# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

word_list = []

def Typoglycemia(my_sentence):
    
    word = my_sentence.split()
    
    for i in range(len(word)):
        if len(word[i]) <= 4:
            word_list.append(word[i])


        else:
            word_body = word[i][1:-1]
            list_body = list(word_body)
            random.shuffle(list_body)
            new_body = ("").join(list_body)
            
            word_shuffle = "%s%s%s" % (word[i][0],new_body,word[i][-1])
            word_list.append(word_shuffle)
            
    
my_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
Typoglycemia(my_sentence)

print (" ").join(word_list)