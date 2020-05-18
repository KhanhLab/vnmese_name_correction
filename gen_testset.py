"""
Created on 2020-05-15

"""

import os.path
import pandas as pd 
import pickle

def get_data(file_path):
    names = pd.read_csv(file_path, sep = '|', header = None, encoding='utf8')
    GT = names[1].map(lambda x: x.replace('GT=','').strip())
    PR = names[2].map(lambda x: x.replace('PR=','').strip())
    CHECK = GT == PR
    data = pd.concat([GT,
                        PR, 
                        CHECK
                       ], axis=1).rename(columns ={1: 'GT', 2:'PR', 0:'CHECK'})
    return data

if __name__=='__main__':
    directory = './data/'
    name_file = "name_result.txt"
    test_file = "test.txt"
    name_path = os.path.join(directory, name_file)
    test_path = os.path.join(directory, test_file)
    test = get_data(name_path)
    with open(test_path, "wb") as p:
        pickle.dump(test, p)