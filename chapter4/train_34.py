# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import argparse
import train_30

def main(neko_dict):
    counter = 0
    for sent in neko_dict:
        for i in range(1,(len(sent)-1)):
            if sent[i-1]["pos"] == "名詞" and sent[i]["pos1"] == "連体化" and sent[i+1]["pos"] == "名詞" :
                counter += 1
                print counter, ":", sent[i-1]["surface"],sent[i]["surface"],sent[i+1]["surface"]

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_file", default="neko.mecab", help="train_34 help")
    args = parser.parse_args()
    morph = train_30.morph(args.input_file)
    main(morph)
    