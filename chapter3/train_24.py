# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
記事から参照されているメディアファイルをすべて抜き出せ．
"""


import argparse

def main(input_file):
    with open(input_file,"r") as in_file :
        for line in in_file :
            if (line.startswith("[[ファイル") == 1) or (line.startswith("[[File") == 1 ):
                print line.rstrip()

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_file", default="./train_20.txt", help = "train help")
    args = parser.parse_args()
    
    main(args.input_file)

    