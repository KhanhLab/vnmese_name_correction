"""
Created on 2020-05-15

"""

import os.path
import pickle
import pandas as pd 

def replace_substr(sentence, pairs):
    for pair in pairs:
        sentence = sentence.replace(pair, pair[0]+' '+pair[1])
    return sentence

if __name__=='__main__':
    directory = './data/'
    pairs_file = "pairs.txt"
    test_file = "test.txt"
    pairs_path = os.path.join(directory, pairs_file)
    test_path = os.path.join(directory, test_file)
    with open(pairs_path, "rb") as p:
        pairs = pickle.load(p)
    test = pd.read_csv(file_path, sep = '|', header = None, encoding='utf8')