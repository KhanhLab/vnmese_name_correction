"""
Created on 2020-05-15

"""

import os.path
import pickle
import pandas as pd 
import time
from fuzzywuzzy import fuzz

def get_file(directory, pairs_name, test_name, last_name):
    with open(os.path.join(directory, pairs_name), "rb") as p:
        pairs = pickle.load(p)
    with open(os.path.join(directory, test_name), "rb") as t:
        test = pickle.load(t)
    with open(os.path.join(directory, last_name), "rb") as l:
        last_names = pickle.load(l)
    return pairs, test, last_names
def replace_substr(sentence, pairs):
    for pair in pairs:
        sentence = sentence.replace(pair, pair[0]+' '+pair[1])
    return sentence

def lastname_match(fullname, last_names):
    scores = []
    lastname = fullname.split(' ')[0]
    for n in last_names:
        score = fuzz.ratio(lastname, n)
        scores.append(score)
    idx = scores.index(max(scores))
    best_match = last_names[idx]
    if len(lastname) == len(best_match):
        return fullname.replace(lastname, best_match)
    else:
        return fullname

if __name__=='__main__':
    start = time.time()
    directory = './data/'
    pairs_name = "pairs.txt"
    test_name = "test.txt"
    last_name = "last.txt"
    pairs, test, last_names = get_file(directory, pairs_name, test_name, last_name)
    test['ARS'] = test['GT'] == test['PR']
    test['CLEAN_PR'] = test['PR'].apply(replace_substr, args = (pairs,))
    test['LASTNAME_PR'] = test['CLEAN_PR'].apply(lastname_match, args = (last_names,))
    test['MOMO'] = test['GT'] == test['LASTNAME_PR']
    print('Done!. Time taken = {:.1f}(s) \n'.format(time.time()-start))
    test.to_excel('test.xlsx', index = 0)
    