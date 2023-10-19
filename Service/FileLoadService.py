from tkinter import filedialog as fd
import os
from CSVFileService import *
from TermFrequencyService import *

def process_data_from_folder():
    folder = fd.askdirectory()
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

process_data_from_folder()

