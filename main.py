import os
import pandas as pd


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


csv_list = list_files('ATC Result 2022-0613', "csv")
print(csv_list)

for scan in csv_list:
    path_parse = scan.split("/")
    #path_parse
    parsed = path_parse[2].split("_")
    print(parsed)

print(csv_list)
