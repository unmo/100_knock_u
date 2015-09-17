# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

"""
import argparse
import re

def main(input_file):
    
    my_dict = {}
    info = re.compile("\|(.*) = (.*)")
    with open(input_file,"r") as in_file :
        for line in in_file:
            i = info.search(line)
            if i is not None:
                my_dict =  line.strip("|").rstrip().split("=")
                print "%s:%s" % (my_dict[0] , my_dict[1])
                
if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser();
    parser.add_argument("-i", "--input", dest = "input_file", default = "train_20.txt", help = "help test")
    args = parser.parse_args()
    main(args.input_file)
    