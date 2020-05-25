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
    """
    Import data for batch testing
    """
    with open(os.path.join(directory, test_file), "rb") as t:
        test = pickle.load(t)
    return test
def vn_correct(word):
    """
    Spelling checking and correction
    """
    word = word.lower()
    check, mispelling = tv.checkTiengViet(word)
    for m in mispelling:
        corrected = tv.correctTiengViet(m)
        word = word.replace(m, corrected)
    return word.upper()
def lastname_match(fullname):
    """
    Matching lastname (optional) 
    """ 
    tokens = fullname.split(' ')
    lastname = tokens[0]
    sm = StringMatching()
    best_match = sm.word_similarity(lastname)
    tokens[0] = best_match
    return ' '.join(tokens)

if __name__=='__main__':
    tv = TiengViet()
    batch = False
    # Batch test: for testing purpose, will be removed soon!
    if batch:
        start = time.time()
        directory = './data/'
        test_file = "test.txt"
        test= get_file(directory, test_file)
        test['ARS'] = test['PR'] == test['GT'] # Check ARS
        test['PUNC'] = test['PR'].map(tv.removePunctuation) # Remove punctuation
        test['CORRECTED_PR'] = test['PUNC'].map(vn_correct) # Spelling correction
        test['LASTNAME_PR'] = test['CORRECTED_PR'].map(lastname_match) # Lastname matching
        test['MOMO'] = test['LASTNAME_PR'] == test['GT'] # Check MOMO
        save_path = 'C:/Users/khanh.trinh/Desktop/'
        test.to_excel(os.path.join(save_path, 'result.xlsx'), index = 0)
        print('Done batch testing!. Time taken = {:.3f}(s) \n'.format(time.time()-start))
    else:
        word = input('Input string:')
        start = time.time()
        word = tv.removePunctuation(word) # Remove punctuation
        word = vn_correct(word) # Spelling correction
        word = lastname_match(word) # Lastname matching
        print(word)
        print('Done testing!. Time taken = {:.3f}(s) \n'.format(time.time()-start))
