from tkinter import filedialog as fd
import os


# return an object with all the files in a given folder
# def load_folder():
#     return


#mock: read and return a list of all file names with .cs
#real: read and return relevant data after processing file; data should be stored in a map?

def process_data_from_folder():
    fileList = []
    folder = fd.askdirectory()
    root_dir = os.path.relpath(folder)
    for root,dirs,files in os.walk(folder):
        for file in files:
            if file.endswith('.cs'):
                fileList.append(os.path.join(os.path.relpath(root_dir,file),file))
    return fileList



filelist = process_data_from_folder()

print(filelist)
