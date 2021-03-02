import os
from pathlib import Path


def read_files_of_directory(directory: str):
    if os.path.exists(directory) and os.path.isdir(directory):
        files_data = []
        content_in_folder = os.listdir(directory)
        content_in_folder.sort()
        for content in content_in_folder:
            file_location = directory + os.path.sep + content
            if os.path.isfile(file_location):
                filename = Path(file_location)
                with open(file_location, 'r', encoding='utf-8') as file:
                    data = ([row.strip().lower() for row in file.readlines()])
                    for x in data:
                        if x == '' or x is None:
                            data.remove(x)
                    if data:
                        files_data.append({filename.stem: data})
        return files_data
    else:
        print('não é um diretorio')



