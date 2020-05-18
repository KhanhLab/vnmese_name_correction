"""
Created on 2020-05-15

"""

import pandas as pd
import os.path
import pickle

def get_dict(dict_path):
    name_dict = pd.read_json(dict_path)
    return name_dict

if __name__=='__main__':
    directory = './data/'
    dict_file = "name_dict.json"
    last_file = "last.txt"
    dict_path = os.path.join(directory, dict_file)
    last_path = os.path.join(directory, last_file)
    name_dict = get_dict(dict_path)
    last_names = name_dict['last_name_group'].map(str.upper).unique()
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(last_path, "wb") as p:
        pickle.dump(last_names, p)