"""
Created on 2020-05-15

"""
import sys
from flask import Flask
from flask import request, abort
from flask import jsonify

import os.path
import time
import pickle
import pandas as pd 
from sources.vietdict import TiengViet
from sources.matching import StringMatching

class VNcorrectAPI():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config["DEBUG"] = True
        self.app.config['JSON_AS_ASCII'] = False
        @self.app.route('/')
        def home():
            return '''<h1>Here we go!</h1>
                    <p>A prototype API for Vietnamese name correction.</p>'''
        @self.app.route('/v1', methods=['GET'])
        def api_correct():
            word = request.args['word']
            if word is None:
                return 'No name provided. Please specify a name!'
            else:
                result = {}
                tv = TiengViet()
                start = datetime.datetime.now()
                word = tv.removePunctuation(word) # Remove punctuation
                word = self.vn_correct(word) # Spelling correction
                print(word)
                result['request_datetime'] = start
                result['fullname'] = word
                return jsonify(result)
        
    def vn_correct(self, word):
        """
        Spelling checking and correction
        """
        tv = TiengViet()
        word = word.lower()
        check, mispelling = tv.checkTiengViet(word)
        for m in mispelling:
            corrected = tv.correctTiengViet(m)
            word = word.replace(m, corrected)
        return word.upper()
    def lastname_match(self, fullname):
        """
        Matching lastname (optional) 
        """ 
        tokens = fullname.split(' ')
        lastname = tokens[0]
        sm = StringMatching()
        best_match = sm.word_similarity(lastname)
        tokens[0] = best_match
        return ' '.join(tokens)

    def run(self, port):
        self.app.run(host='0.0.0.0',port=port)

if __name__=='__main__':
    args = sys.argv
    if len(args) > 1:
        port = int(args[1])
    else:
        port = 8080
    service = VNcorrectAPI()
    service.run(port)
