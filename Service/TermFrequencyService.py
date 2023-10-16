import os
import re

if_pattern = r'if\s*\(.+?\)'
for_pattern = r'\b(for|foreach)\s*\([^)]*\)' #also counts foreach loops as well
while_pattern = r'while\s*\(.+?\)'

def get_number_of_ifs(folder):
    ifs = 0
    for root,dirs,files in os.walk(folder):
        for file_name in files:
            with open(os.path.join(root, file_name), 'r',encoding='utf8',errors='ignore') as file:
                code = file.read()
            if file_name.endswith('.cs'):
                if_matches = re.findall(if_pattern,code,re.MULTILINE)
                ifs += len(if_matches)
    return ifs

def get_number_of_fors(folder):
    fors = 0
    for root,dirs,files in os.walk(folder):
        for file_name in files:
            with open(os.path.join(root, file_name), 'r',encoding='utf8',errors='ignore') as file:
                code = file.read()
            if file_name.endswith('.cs'):
                for_matches = re.findall(for_pattern,code,re.MULTILINE)
                fors += len(for_matches)
    return fors

def get_number_of_whiles(folder):
    whiles = 0
    for root,dirs,files in os.walk(folder):
        for file_name in files:
            with open(os.path.join(root, file_name), 'r',encoding='utf8',errors='ignore') as file:
                code = file.read()
            if file_name.endswith('.cs'):
                while_matches = re.findall(while_pattern,code,re.MULTILINE)
                whiles += len(while_matches)
    return whiles

