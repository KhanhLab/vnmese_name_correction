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

    def gen_pairs(self, cons, cons_comb):
        pairs = []
        for pair in list(itertools.combinations(cons, 2)):
            s = pair[0]+pair[1]
            pairs.append(s)
        pairs = set(pairs)
        pairs.difference_update(cons_comb)
        return pairs

if __name__=='__main__':
    process = Processor()
    pairs = process.gen_pairs(process.cons, process.cons_comb)
    directory = './data/'
    pairs_name = "pairs.txt"
    pairs_path = os.path.join(directory, pairs_name)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(pairs_path, "wb") as p:
        pickle.dump(pairs, p)

    