# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import argparse

class Morph:
    def __init__(self, line):
        surface, features = line.strip().split("\t")
        features = features.split(",")
        self.surface = surface
        self.base = features[6]
        self.pos = features[0]
        self.pos1 = features[1]


def main(in_file):
    with open(in_file,"r") as fin :
        sentence = list()
        sentences = list()
        
        for line in fin:
            if line.startswith("* "):
                continue
            elif line == "EOS\n":
                sentences.append(sentence)
                sentence = list()
            else:
                sentence.append(Morph(line))
                
        print " ".join([morph.surface for morph in sentences[3]])
   
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="cabocha", default="neko.txt.cabocha", help="train_50 help")
    args = parser.parse_args()
    main(args.cabocha)
    
    
    
        
        
