from tkinter import filedialog as fd
import os
import re
from CSVFileService import *


#TODO: add filter to ignore assembly files and migrations
#TODO: refactor regex for usings and method identification
def process_data_from_folder():
    filePathName = []
    fileName = []
    folder = fd.askdirectory()
    exclude = set['.git','.idea','bin','obj']
    method_pattern = r'[a-zA-Z][a-zA-Z0-9]+\([a-zA-Z][a-zA-Z0-9]+\)'
    usings_pattern = r'^using\s+[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*;$'

    for root,dirs,files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in exclude]

        for file_name in files:
            if file_name.endswith('.cs'):
                file_rel_path = os.path.relpath(os.path.join(root, file_name), folder).replace("\\", "/")
                filePathName.append(file_rel_path)

                fileName.append(file_name)

                with open(os.path.join(root,file_name), 'r') as file:
                    code = file.read()
                    method_matches = re.findall(method_pattern, code)
                    usings_matches = re.findall(usings_pattern,code)

                parent_dir = os.path.basename(os.path.dirname(file_rel_path))
                row = [parent_dir, file_rel_path, file_name, method_matches, usings_matches]
                write_row_to_csv(row)

process_data_from_folder()

