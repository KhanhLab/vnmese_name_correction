"""
Created on 2020-05-15

"""

import numpy as np

vows = ["a", "ă", "â", "e", "ê", "i", "y", "o", "ô", "ơ", "u", "ư"]
cons = ["b", "c", "d", "đ", "g", "h", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x"]
chars = vows + cons

vow_comb = ["ai", "ao", "au", "âu", "ay", "ây", "eo", "êu", "ia", "iê", "yê", 
            "iu", "oa", "oă", "oe", "oi", "ôi", "ơi", "oo", "ôô", "ua", "uă", 
            "uâ", "ưa", "uê", "ui", "ưi", "uo", "uô", "uơ", "ươ", "ưu", "uy",
            "iêu", "yêu", "oai", "oao", "oay", "oeo", "uao", "uây", "uôi", "ươi", "ươu", "uya", "uyê", "uyu"]
cons_comb = ["ch", "gh", "kh", "ng", "ngh", "nh", "ph", "th", "tr", "gi", "qu"]
pairs = vow_comb + cons_comb

def gen_cmatrix(chars,pairs):
    n =len(chars)
    M = np.zeros((n,n), dtype=int)
    for i in range(0,n):
        for j in range(0,n):
            s = chars[i]+chars[j]
            if s in pairs:
                M[i,j]=1
            else:
                continue    
    return M
M = gen_cmatrix(chars,pairs)

