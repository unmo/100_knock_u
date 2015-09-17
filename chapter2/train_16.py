# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import argparse

def main(num,input_file):
    with open(input_file,"r") as read_file :
        line = read_file.readlines()
        for n in range(num):
            with open("%s_%d.txt" % ("split",n+1) ,"w") as split:
                split.write(line[n])

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', dest = 'num', default = 3)
    parser.add_argument('-i', '--input', dest = 'input_file', default = "../data/hightemp.txt")
    args = parser.parse_args()
    main(args.num,args.input_file)


