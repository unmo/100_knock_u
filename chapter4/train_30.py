# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型(辞書型)に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import argparse

def morph(input_file):    
    neko_list = list()
    neko_dict = list()    
    morph = dict()
    
    with open(input_file,"r") as in_file:
        
        for line in in_file:
            
            if line.startswith('EOS') or line == "":
                neko_dict.append(neko_list)
                neko_list = list()
                continue

            surface,items = line.strip().split("\t")
            items_list = items.split(",")
            
            morph = {"surface":surface, "base":items_list[6], "pos":items_list[0], "pos1":items_list[1] }
            neko_list.append(morph)
            
        return neko_dict
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "input_file", default="neko.mecab", help="train 30 input file")
    args = parser.parse_args()
    morph = morph(args.input_file)
    
