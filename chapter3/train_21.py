# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
記事中でカテゴリ名を宣言している行を抽出せよ．

"""
import sys

with open(sys.argv[1],"r") as read_file:
    for line in read_file:
        if line.find('Category') != -1:
            print u"%s" % line