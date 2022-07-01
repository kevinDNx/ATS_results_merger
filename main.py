import os
import glob
import pandas as pd


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


csv_list = list_files('ATC Result 2022-0613', "csv")
#TODO: insert function to sort csv_list by date
#print(csv_list)
snum_list = []
for scan in csv_list:
    path_parse = scan.split("/")
    # path_parse
    parsed = path_parse[2].split("_")
    # print(parsed)
    snum = parsed[0]
    if snum not in snum_list:
        snum_list += [snum]
        merge_list = list(filter(lambda x: snum in x, csv_list))
        press_list = list(filter(lambda x: 'press' in x, merge_list))
        temp_list = list(filter(lambda x: 'Temp' in x, merge_list))
        #print(merge_list)
        #print(press_list)
        #print(temp_list)
        #TODO: combine all elements in press_list and temp_list.
        press_combine = pd.concat([pd.read_csv(f) for f in press_list])
        #print(press_combine)
        temp_combine = pd.concat([pd.read_csv(f) for f in temp_list])
        print(temp_combine)
        #TODO: make a writer to write the list of csv files to the same output file and sheet
        # Use snum, press_list, and merge_list.
