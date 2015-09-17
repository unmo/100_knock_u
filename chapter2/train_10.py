# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

with open("../data/hightemp.txt","r") as my_file:
    print len(my_file.readlines())
    


