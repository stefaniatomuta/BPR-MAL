from tkinter import filedialog as fd
import os

# return an object with all the files in a given folder
def load_folder():
    return os.listdir(fd.askdirectory())

def file_names_in_folder(folder):
    fileList = [""]
    i: int = 0
    for filename in folder:
        fileList.insert(i, filename.title())
        i += 1
    return fileList


#TODO: read all files from subfolders

filelist = file_names_in_folder(load_folder())

print(filelist)
