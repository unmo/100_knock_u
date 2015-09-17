# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

"""
count = 0

with open("../data/hightemp.txt","r") as read_file , open("translate_11.txt","w") as write_file :
    for line in read_file:
        temp = line.replace("\t"," ")
        write_file.writelines(temp)
        
