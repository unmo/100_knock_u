# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""
import argparse

def merge(col1,col2):
    with open("merge.txt","w") as merge:
        for a,b in zip(open(col1,"r"),open(col2,"r")):
            a = a.strip()
            b = b.strip()
            merge.write(a + "\t"+ b + "\n")
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-c1', '--col1', dest = 'col1', default="col1.txt")
    parser.add_argument('-c2', '--col2', dest = 'col2', default="col2.txt")
    args = parser.parse_args()
    merge(args.col1,args.col2)

