# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015
@author: umezawa
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import argparse
import train_30

def main(neko_dict):
    nouns = list()
    for sent in neko_dict:
        for m in sent:
            if m["pos"] == "名詞" :
                nouns.append(m["surface"])
            elif nouns:
                print ("+").join(nouns)
                nouns = list()
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_file", default="neko.mecab", help="train_35 help")
    args = parser.parse_args()
    morph = train_30.morph(args.input_file)
    main(morph)
    