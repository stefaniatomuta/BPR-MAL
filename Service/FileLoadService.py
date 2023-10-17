from tkinter import filedialog as fd
import os
import re
from CSVFileService import *
from TermFrequencyService import *


#TODO: add filter to ignore assembly files and migrations
#TODO: refactor regex for usings and method identification
def process_data_from_folder():
    filePathName = []
    fileName = []
    folder = fd.askdirectory()
    exclude = {'.git', '.idea', 'bin', 'obj'}
    fors = 0
    ifs = 0
    whiles = 0
    foreaches = 0
    for root,dirs,files in os.walk(folder):
        for file_name in files:
            if file_name.endswith('.cs'):
                file_path = os.path.join(root,file_name)
                fors += get_number_of_fors_in_file(file_path)
                ifs += get_number_of_ifs_in_file(file_path)
                whiles += get_number_of_whiles_in_file(file_path)
                foreaches += get_number_of_foreaches_in_file(file_path)

    row = [fors,foreaches,ifs,whiles]
    write_row_to_csv(row)
    # for root,dirs,files in os.walk(folder):
    #     dirs[:] = [d for d in dirs if d not in exclude]
    #
    #     for file_name in files:
    #         if file_name.endswith('.cs'):
    #             file_rel_path = os.path.relpath(os.path.join(root, file_name), folder).replace("\\", "/")
    #             filePathName.append(file_rel_path)
    #
    #             fileName.append(file_name)
    #
    #             with open(os.path.join(root,file_name), 'r') as file:
    #                 code = file.read()
    #                 method_matches = re.findall(method_pattern, code)
    #                 usings_matches = re.findall(usings_pattern,code,re.MULTILINE)
    #             parent_dir = os.path.basename(os.path.dirname(file_rel_path))
    #             row = [parent_dir, file_rel_path, file_name, method_matches, usings_matches]
    #             write_row_to_csv(row)

process_data_from_folder()

