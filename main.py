import os
import pandas as pd
import dask.dataframe as dd
import numpy

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
        #TODO: combine all elements in press_list and temp_list. Maybe add the date columns before combining
        press_combine = dd.concat([dd.read_csv(f).assign(SN=f.split("/")[2].split("_")[0]).assign(
            Date=pd.to_datetime(f.split("/")[2].split("_")[1])) for f in press_list])
        print(press_combine)
        press_combine.to_csv('%s_press.csv' % (snum), single_file=1)

        temp_combine = dd.concat([dd.read_csv(f).assign(SN=f.split("/")[2].split("_")[0]).assign(
            Date=pd.to_datetime(f.split("/")[2].split("_")[1])) for f in temp_list])
        print(temp_combine)
        temp_combine.to_csv('%s_temp.csv' % (snum), single_file=1)
        #TODO: make a writer to write the list of csv files to the same output file and sheet
        # Use snum, press_list, and merge_list.
        #break
    #break
