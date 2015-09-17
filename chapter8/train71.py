# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．
"""

import argparse

def check_stoplist(word):
    check = 0
    with open("stopwords.txt","r") as s_list:
        for line in s_list:    
            if word in line :
                check = True
                return check
                
            elif word not in line :                
                check = False
            
        return check
                
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", dest = "word", default = "there")
    args = parser.parse_args()
    
    check = check_stoplist(args.word)
    print check
