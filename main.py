"""
Created on 2020-05-15

"""

import os.path
import pickle

if __name__=='__main__':
    directory = './data/'
    filename = "pairs.txt"
    file_path = os.path.join(directory, filename)
    with open(file_path, "rb") as p:
        pairs = pickle.load(p)
    