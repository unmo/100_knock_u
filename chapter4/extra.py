# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import argparse
import sys
import MeCab

def main(input_file, output_file):
    tagger = MeCab.Tagger("-Ochasen")
    
    with open(input_file,"r") as in_file, open(output_file,"w") as out_file:
        for line in in_file:
            result = tagger.parse(line)
            out_file.write(result)
            
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "input_file", default="neko.txt", help="extra train input")
    parser.add_argument("-o", "--output", dest = "output_file", default="neko.txt.mecab", help="extra train output")
    args = parser.parse_args()
    main(args.input_file,args.output_file)
    