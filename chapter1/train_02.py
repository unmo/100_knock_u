# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""

# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
# ZIP関数

str1 = u"パトカー"
str2 = u"タクシー"
str3 = u""

for s1,s2 in zip(str1,str2):
    str3 += s1
    str3 += s2
    
print str3