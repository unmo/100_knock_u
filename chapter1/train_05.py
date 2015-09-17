# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def word_ngram(my_sent,ngram):
    word_split = []
    words = ["<s>"] + my_sent.split()
    words.append("</s>")
    
    for i in range(len(words) - ngram + 1 ):
        word_split.append(words[i:i+ngram])
    
    return word_split
    
def char_ngram(my_sent,ngram):
    return "char_ngram"
    
    
    
my_sent = "I am an NLPer"
num = 2

print word_ngram(my_sent,num)
print char_ngram(my_sent,num)