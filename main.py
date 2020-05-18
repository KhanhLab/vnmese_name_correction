"""
Created on 2020-05-15

"""

import os.path
import pickle
import pandas as pd 

def get_file(directory, pairs_name, test_name):
    with open(os.path.join(directory, pairs_name), "rb") as p:
        pairs = pickle.load(p)
    with open(os.path.join(directory, test_name), "rb") as t:
        test = pickle.load(t)
    return pairs, test 
def replace_substr(sentence, pairs):
    for pair in pairs:
        sentence = sentence.replace(pair, pair[0]+' '+pair[1])
    return sentence

if __name__=='__main__':
    directory = './data/'
    pairs_name = "pairs.txt"
    test_name = "test.txt"
    pairs, test = get_file(directory, pairs_name, test_name)
    