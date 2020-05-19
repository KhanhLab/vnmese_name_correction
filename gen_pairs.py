"""
Created on 2020-05-15

"""
import itertools
import codecs
import os.path
import pickle


class Processor:
    def __init__(self):
        self.vows = ["A", "Ă", "Â", "E", "Ê", "I", "Y", "O", "Ô", "Ơ", "U", "Ư"]
        self.cons = ["B", "C", "D", "Đ", "G", "H", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X"]
        self.cons_comb = ["CH", "GH", "KH", "NG", "NGH", "NH", "PH", "TH", "TR", "GI"]
        self.cons_after = ["C","M", "N", "P", "T"]
    def gen_pairs(self, cons, cons_comb, vows, cons_after):
        # cons combination
        con_pairs = [] 
        for c in list(itertools.product(cons, repeat=2)):
            _c = c[0]+c[1]
            con_pairs.append(_c)
        con_pairs = set(con_pairs)
        con_pairs.difference_update(cons_comb)
        # con-vow combination
        cons_notafter = set(cons).difference(cons_after)
        vowcon_pairs = [] 
        for vc in list(itertools.product(vows,cons_notafter)):
            _vc = vc[0]+vc[1]
            vowcon_pairs.append(_vc)
        vowcon_pairs = set(vowcon_pairs)
        # combine results
        pairs = con_pairs.union(vowcon_pairs)
        return pairs

if __name__=='__main__':
    process = Processor()
    pairs = process.gen_pairs(process.cons, process.cons_comb, process.vows, process.cons_after)
    directory = './data/'
    pairs_file = "pairs.txt"
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(os.path.join(directory, pairs_file), "wb") as p:
        pickle.dump(pairs, p)

    