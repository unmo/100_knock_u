# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import train_30
import argparse
from collections import Counter


def main(neko_dict):
    word_list = list()    
    for neko_list in neko_dict:
        for m in neko_list:
            word_list.append(m["surface"])
        
    for word, count in Counter(word_list).most_common():
        print count ,":", word

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_file", default="neko.mecab", help="train_36 help")
    args = parser.parse_args()
    morph = train_30.morph(args.input_file)
    main(morph)
    