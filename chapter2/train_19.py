# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

import argparse
from collections import Counter

cols_list = []

def main(input_file):
    with open(input_file,"r") as in_file:
        for line in in_file:
            cols = line.split("\t")[0]
            cols_list.append(cols)
        #print cols_list
        count = Counter(cols_list)
        #print count
        for k,v in sorted(count.items(), key=lambda x:x[1], reverse = True):
            print "%s:%d" % (k,v)
        
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",dest="input",default="../data/hightemp.txt")
    args = parser.parse_args()
    main(args.input)
