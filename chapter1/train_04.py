# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

my_sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = my_sent.split(" ")

my_dict = {}

head = [1,5,6,7,8,9,15,16,19]

for i in range(len(words)):
    if i+1 in head:
        str1 = words[i]
        str2 = str1[0:1]
        my_dict[words[i][0:1]] = i+1
        
    else :
        str1 = words[i]
        str2 = str1[0:2]
        my_dict[words[i][0:2]] = i+1
        
for key,value in sorted(my_dict.items(), key=lambda x:x[1]):
    print key ,":" , value

