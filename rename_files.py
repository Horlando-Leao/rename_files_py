"""
Script python para renomar todos os arquivos de um diretorio
Os nomes serão uma cadeia de caracteres aleatorios
Esse script recebe apenas dois argumentos posicionais: 
1=<Caminho do diretorio>, 
2=<extensão do arquivo para match>.
"""

import os
import sys
import uuid

sys.argv[0]='rename_files.py'


PATH_FILES = str(sys.argv[1]) #path directory
EXTESION_FILES = str(sys.argv[2]).lower()# set extension pdf or doc or others, without dot "."


def get_list_name_files(APP_FOLDER:str,) -> list:

    NameFiles = []
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching files in : ',base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                NameFiles.append(Files)
    return NameFiles

def get_number_of_files(APP_FOLDER:str) -> int:

    totalFiles = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching number of files in : ',base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                totalFiles += 1
    print('Total number of files',totalFiles)
    return int(totalFiles)

if __name__ == '__main__' and get_number_of_files(PATH_FILES) > 0:
    list_files = get_list_name_files(PATH_FILES)
    for file in list_files:
        old_name_file = f'{PATH_FILES}/{file}'
        new_name_file = f'{PATH_FILES}/{str(uuid.uuid4())}.{EXTESION_FILES}'
        os.rename(old_name_file, new_name_file)


