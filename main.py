"""
Created on 2020-05-15

"""

import os.path
import pickle
import pandas as pd 
import time
from fuzzywuzzy import fuzz

def get_file(directory, pairs_file, test_file, lastname_file):
    with open(os.path.join(directory, pairs_file), "rb") as p:
        pairs = pickle.load(p)
    with open(os.path.join(directory, test_file), "rb") as t:
        test = pickle.load(t)
    with open(os.path.join(directory, lastname_file), "rb") as l:
        lastnames_dict = pickle.load(l)
    return pairs, test, lastnames_dict
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
    pairs_file = "pairs.txt"
    test_file = "test.txt"
    lastname_file = "last.txt"
    pairs, test, lastnames_dict = get_file(directory, pairs_file, test_file, lastname_file)
    test['ARS'] = test['GT'] == test['PR']
    test['CLEAN_PR'] = test['PR'].apply(replace_substr, args = (pairs,))
    test['LASTNAME_PR'] = test['CLEAN_PR'].apply(lastname_match, args = (lastnames_dict,))
    test['MOMO'] = test['GT'] == test['LASTNAME_PR']
    print('Done!. Time taken = {:.1f}(s) \n'.format(time.time()-start))
    test.to_excel('test.xlsx', index = 0)
    