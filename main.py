# Update 06/30/2022, 3:26 PM:
# Took code from https://stackoverflow.com/questions/17025300/dictionary-of-folders-and-subfolders
# to act as a framework to navigate the files
import pandas as pd
import os

master_List = []


def get_listings(directory):

    parent, folder = os.path.split(directory)  # splits a file pathname into a head and a tail
    listings = {
        'folder': folder,
        'children-files': [],
        'children-folders': [],
    }

    children = os.listdir(directory)
    for child in children:
        child_path = os.path.join(directory, child)
        if os.path.isdir(child_path):
            listings['children-folders'] += [get_listings( child_path )]
        else:
            listings['children-files'] += [child]
            if ~('.html' in child):
                master_List.append(child)
                print(child, "added to master_List")

    #TODO: sorting csv files into lists based on serial number.
    #TODO: sorting these lists based on date
    #TODO: splitting this lists into two: press/Temp
    #TODO: output combined csv files with the name based on the serial number and press/Temp


    return listings


t_directory = './ATC Result 2022-0613'
get_listings(t_directory)
print(master_List)

