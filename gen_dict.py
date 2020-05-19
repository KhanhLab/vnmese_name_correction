"""
Created on 2020-05-15

"""

import pandas as pd
import os.path
import pickle

def get_json(directory, filename):
    file_path = os.path.join(directory, filename)
    file_dict = pd.read_json(file_path)
    return file_dict

if __name__=='__main__':
    directory = './data/'
    json_file = "fullname_dict.json"
    lastname_file = "last.txt"
    fullname_dict = get_json(directory, json_file)
    lastname_dict = fullname_dict['last_name_group'].map(str.upper).unique()
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(os.path.join(directory, lastname_file), "wb") as p:
        pickle.dump(lastname_dict, p)