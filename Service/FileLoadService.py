from tkinter import filedialog as fd
import os
import re
from sklearn.feature_extraction.text import CountVectorizer

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


#TODO: add filter to ignore assembly files

def process_data_from_folder():
    filePathName = []
    fileName = []
    methodName = {}
    folder = fd.askdirectory()
    root_dir = os.path.basename(folder)
    exclude = set['.git','.idea','bin','obj']
    for root,dirs,files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith('.cs'):
                filePathName.append(get_relpath(root_dir,file))
                fileName.append(os.path.basename(file))
                methodName = get_method_name_from_folder(os.path.join(root, file),root_dir)

    return filePathName,filePathName,methodName


#TODO: refactor relpath
#gets a set of all method names + their file location
def get_method_name_from_folder(file_path,root):
    method_pattern = r'[a-zA-Z][a-zA-Z0-9]+\('
    method_info = {}
    with open(file_path, 'r') as file:
        code = file.read()
        method_matches = re.findall(method_pattern, code)
        for method_name in method_matches:
            method_info[method_name] = get_relpath(root,file_path)

    return method_info

filelist,filepathlist,filemethodlist = process_data_from_folder()
# filelistProccessed = process_text(filelist)

print(filemethodlist)
