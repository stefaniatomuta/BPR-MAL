from tkinter import filedialog as fd
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from CSVFileService import *

# return an object with all the files in a given folder
# def load_folder():
#     return
def process_text(text):
    vect = CountVectorizer(max_features=10000).fit(text)
    return vect.transform(text)

def get_relpath(root,file):
    relative_path = os.path.relpath(os.path.join(root, file))
    return relative_path.replace("\\", "/")


#mock: read and return a list of all file names with .cs
#real: read and return relevant data after processing file; data should be stored in a map?


#TODO: add filter to ignore assembly files and migrations

def process_data_from_folder():
    filePathName = []
    fileName = []
    folder = fd.askdirectory()
    root_dir = os.path.basename(folder)
    exclude = set['.git','.idea','bin','obj']
    method_pattern = r'[a-zA-Z][a-zA-Z0-9]+\([a-zA-Z][a-zA-Z0-9]+\)'

    for root,dirs,files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in exclude]

        for file_path in files:
            if file_path.endswith('.cs'):
                file_rel_path = get_relpath(root_dir,file_path)
                filePathName.append(file_rel_path)

                file_name = os.path.basename(file_path)
                fileName.append(file_name)

                with open(os.path.join(root,file_path), 'r') as file:
                    code = file.read()
                    method_matches = re.findall(method_pattern, code)
                    method_names = {}
                    for method_name in method_matches:
                        method_names[method_name] = get_relpath(root, file_path)
                        row = [root_dir, file_rel_path, file_name, method_name]
                        write_row_to_csv(row)

    return filePathName,filePathName,method_names

#TODO: refactor relpath
#gets a set of all method names + their file location
# def get_method_name_from_folder(file_path,root):
#
#
#     return method_info

filelist,filepathlist,filemethodlist = process_data_from_folder()
# filelistProccessed = process_text(filelist)

print(filelist)
