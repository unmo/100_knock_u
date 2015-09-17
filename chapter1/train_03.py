# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""

#　"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#  という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．


my_sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words_len = []
words = my_sent.split()
for word in words:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1]
    words_len.append(len(word))

print words_len

