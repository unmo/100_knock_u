# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
サ変接続の名詞をすべて抽出せよ．
"""

import argparse
import train_30

def main(neko_dict):
    count = 0
    for sent in neko_dict :
        for m in sent :
            if m["pos1"] == "サ変接続" :
                count += 1
                print count ,":" , m["surface"]
    
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser();
    parser.add_argument("-i", "--input", dest="input_file", default="neko.mecab", help = "train32 help")
    args = parser.parse_args()
    morph = train_30.morph(args.input_file)
    main(morph)
    