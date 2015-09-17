# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015
@author: umezawa
@
"""

# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

str = u"パタトクカシーー"
str_list = [str[0],str[2],str[4],str[6]]
print "".join(str_list)