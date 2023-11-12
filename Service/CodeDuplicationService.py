import os
import gensim
import tempfile
from enum import Enum
from nltk.tokenize import word_tokenize
from collections import OrderedDict
import numpy as np

source_code_file_extensions = ["h", "c", "cpp", "cc", "java", "py", "cs"]
file_column_label = "File"
file_loc_label = ",#LoC"
similarity_column_label = "Similarity (%)"
similarity_label_length = len(similarity_column_label)
loc_label = "#LoC"
similarity_label = "Similarity"
fail_threshold = 100
ignore_threshold = 0


# """Get a list with all the source code files within the directory"""
def get_all_source_code_from_directory(directory, file_extensions):
    source_code_files = list()
    for dirpath, _, filenames in os.walk(directory):
        for name in filenames:
            _, file_extension = os.path.splitext(name)
            if file_extension[1:] in file_extensions:
                filename = os.path.join(dirpath, name)
                source_code_files.append(filename)

    return source_code_files


# lines of code count
def get_loc_count(file_path):
    lines_count = -1
    try:
        with open(os.path.normpath(file_path), 'r') as the_file:
            lines_count = len(the_file.readlines())
    except Exception as err:
        print(f"WARNING: Failed to get lines count for file {file_path}, reason: {str(err)}")
    return lines_count


def get_loc_to_print(loc_count):
    loc_to_print = str(loc_count) if loc_count >= 0 else ""
    return loc_to_print


def get_proj_root_dir(project_root_dir):
    if project_root_dir:
        project_root_dir = os.path.abspath(project_root_dir)
        project_root_dir = os.path.join(project_root_dir, "")
    return project_root_dir


def parse_source_code(source_code_files):
    source_code = OrderedDict()
    for source_code_file in source_code_files:
        try:
            # read file but also recover from encoding errors in source files
            with open(source_code_file, "r", errors="surrogateescape") as f:
                # Store source code with the file path as the key
                content = f.read()
                source_code[source_code_file] = content
        except Exception as err:
            print(f"ERROR: Failed to open file {source_code_file}, reason: {str(err)}")
    return source_code


def get_source_code_files(directory, file_extensions):
    source_code_files = list()
    files_to_ignore = list()
    source_code_files += get_all_source_code_from_directory(directory, file_extensions)
    source_code_files = [os.path.normpath(f) for f in source_code_files]
    source_code_files = list(set(source_code_files) - set(files_to_ignore))
    # Sort the sources, so the results are sorted too and are reproducible
    source_code_files.sort()
    source_code_files = [os.path.abspath(f) for f in source_code_files]
    return source_code_files


def get_code_similarity(directory):
    source_code_files = get_source_code_files(directory, 'cs')
    proj_root_dir = get_proj_root_dir(directory)
    source_code = parse_source_code(source_code_files)
    # Create a Similarity object of all the source code
    gen_docs = [
        [word.lower() for word in word_tokenize(source_code[source_file])]
        for source_file in source_code
    ]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity(tempfile.gettempdir() + os.sep, tf_idf[corpus], num_features=len(dictionary))

    code_similarity = dict()
    for source_file in source_code:
        # Check for similarities
        query_doc = [w.lower() for w in word_tokenize(source_code[source_file])]
        query_doc_bow = dictionary.doc2bow(query_doc)
        query_doc_tf_idf = tf_idf[query_doc_bow]

        short_source_file_path = source_file.replace(proj_root_dir, "")

        empty_length = 0
        code_similarity[short_source_file_path] = dict()
        for similarity, source in zip(sims[query_doc_tf_idf], source_code):
            # Ignore similarities for the same file
            if source == source_file:
                continue
            similarity_percentage = similarity * 100
            # Ignore very low similarity
            if similarity_percentage < ignore_threshold:
                continue
            short_source_path = source.replace(proj_root_dir, "")
            code_similarity[short_source_file_path][short_source_path] = round(similarity_percentage, 2)

        # If no similarities found for the particular file, remove it from the report
        if len(code_similarity[short_source_file_path]) == empty_length:
            del code_similarity[short_source_file_path]
    return code_similarity


def get_code_similarity_matrix(folder_path):
    code_similarity = get_code_similarity(folder_path)
    all_values = [value for sub_dict in code_similarity.values() for value in sub_dict.values()]
    num_items = len(code_similarity)
    matrix = np.zeros((num_items, num_items), dtype=int)
    for i in range(num_items):
        for j in range(num_items):
            if i != j:
                matrix[i, j] = all_values.pop(0)
    return matrix
