import os
import pandas as pd
import dask.dataframe as dd # this library is probably not used.
import numpy

# This code uses magic numbers and symbols that may not be consistent on different systems.
# It accounts for only a few filepath string variations, as follows: 
# 'C:\\ATC Result 2020-0613\\2022-0107\\11020434_20220107_1355_press.csv', 
# 'C:\\ATC Result 2020-0613\\2022-0124\\Morning\\11020434_2022124_0932_press.csv' ## Morning, Modified script, Unmodified script
# There are a lot of print statements. Feel free to delete them.
def list_files(filepath, filetype): # helper method to create a list of specified filetypes within a directory.
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


def parseHelper(badParse): # helper method to help parse variations in filepath names
    if 'Modified script' in badParse or 'Unmodified script' in badParse or 'Morning' in badParse:
        return badParse.split("\\")[4].split("_")
    else:
        return badParse.split("\\")[3].split("_")
                                             
csv_list = list_files('C:\ATC Result 2020-0613', "csv") # getting the list of csv files in ATC Result 2020-0613
snum_list = [] # this list is to keep track of serial numbers that we have already outputted so we don't reuse them.

#print(csv_list)

for scan in csv_list:
    # The section below checks for the serial number.
    snum = parseHelper(scan)[0]
    #print(scan.split("\\")[3].split("_")[0])
    print(snum)
    
    if snum not in snum_list: # where snum_list comes into play
        snum_list += [snum]
        merge_list = list(filter(lambda x: snum in x, csv_list))
        press_list = list(filter(lambda x: 'press' in x, merge_list))
        temp_list = list(filter(lambda x: 'Temp' in x, merge_list))
        #print(merge_list)
        print(press_list)
        #print(temp_list)
        # The section below is where the files are combined into SN_press.csv and SN_temp.csv
        press_combine = pd.concat([pd.read_csv(f).assign(SN=parseHelper(f)[0]).assign(
            Date=parseHelper(f)[1]) for f in press_list], ignore_index=1)
        print(press_combine)
        press_combine.to_csv('%s_press.csv' % (snum))

        temp_combine = pd.concat([pd.read_csv(f).assign(SN=parseHelper(f)[0]).assign(
            Date=parseHelper(f)[1]) for f in temp_list], ignore_index=1)
        print(temp_combine)
        temp_combine.to_csv('%s_temp.csv' % (snum))
        #break
    #break
