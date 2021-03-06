"""
Created on 2020-05-15

"""

import os.path
import pandas as pd 
import pickle

def get_data(directory, filename):
    file_path = os.path.join(directory, filename)
    names = pd.read_csv(file_path, sep = '|', header = None, encoding='utf8')
    GT = names[1].map(lambda x: x.replace('GT=','').strip())
    PR = names[2].map(lambda x: x.replace('PR=','').strip())
    # CHECK = GT == PR
    data = pd.concat([GT,
                        PR, 
                        # CHECK
                       ], axis=1).rename(columns ={1: 'GT', 2:'PR', 0:'CHECK'})
    return data

if __name__=='__main__':
    directory = './data/'
    name_file = "name_result.txt"
    test_file = "test.txt"
    test = get_data(directory, name_file)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(os.path.join(directory, test_file), "wb") as p:
        pickle.dump(test, p)