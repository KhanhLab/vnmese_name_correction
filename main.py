"""
Created on 2020-05-15

"""

import os.path
import pickle
import pandas as pd 
import time
from fuzzywuzzy import fuzz
from vietdict import TiengViet

def get_file(directory, test_file, lastname_file):
    with open(os.path.join(directory, test_file), "rb") as t:
        test = pickle.load(t)
    with open(os.path.join(directory, lastname_file), "rb") as l:
        lastnames_dict = pickle.load(l)
    return test, lastnames_dict
def vn_correct(word):
    word = word.lower()
    check, mispelling = tv.checkTiengViet(word)
    for m in mispelling:
        corrected = tv.correctTiengViet(m)
        word = word.replace(m, corrected)
    return word.upper()

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
    tv = TiengViet()
    start = time.time()
    directory = './data/'
    test_file = "test.txt"
    lastname_file = "last.txt"
    test, lastnames_dict = get_file(directory, test_file, lastname_file)
    test['CORRECTED_PR'] = test['PR'].map(vn_correct)
    test['ARS'] = test['PR'] == test['GT']
    test['MOMO'] = test['CORRECTED_PR'] == test['GT']
    # test.to_excel('test.xlsx', index = 0)
    print('Done!. Time taken = {:.1f}(s) \n'.format(time.time()-start))