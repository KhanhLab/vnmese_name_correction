"""
Created on 2020-05-15

"""

import os.path
import time
import pickle
import pandas as pd 
from sources.vietdict import TiengViet
from sources.matching import StringMatching

def get_file(directory, test_file):
    with open(os.path.join(directory, test_file), "rb") as t:
        test = pickle.load(t)
    return test
def vn_correct(word):
    word = word.lower()
    check, mispelling = tv.checkTiengViet(word)
    for m in mispelling:
        corrected = tv.correctTiengViet(m)
        word = word.replace(m, corrected)
    return word.upper()
def lastname_match(fullname):
    lastname = fullname.split(' ')[0]
    sm = StringMatching()
    best_match = sm.word_similarity(lastname)
    return fullname.replace(lastname, best_match)

if __name__=='__main__':
    tv = TiengViet()
    start = time.time()
    directory = './data/'
    test_file = "test.txt"
    test= get_file(directory, test_file)
    test['ARS'] = test['PR'] == test['GT'] # Check ARS
    test['PUNC'] = test['PR'].map(tv.removePunctuation) # Remove punctuation
    test['CORRECTED_PR'] = test['PUNC'].map(vn_correct) # Spelling correction
    test['LASTNAME_PR'] = test['CORRECTED_PR'].map(lastname_match) # Lastname matching
    test['MOMO'] = test['LASTNAME_PR'] == test['GT'] # Check MOMO
    test.to_excel('test.xlsx', index = 0)
    print('Done!. Time taken = {:.1f}(s) \n'.format(time.time()-start))