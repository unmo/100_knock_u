# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""
import argparse


def extract(file_name):
    with open(file_name,"r") as read,  open("col1.txt","w") as col1 , open("col2.txt","w") as col2:
        for line in read:
            itemList = line.rstrip().split('\t')
            col1.write(itemList[0]+"\n")
            col2.write(itemList[1]+"\n")
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="extraction function test")
    parser.add_argument('-t', '--train' , dest = 'train' ,default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()    
    print args.train
    extract(args.train)

