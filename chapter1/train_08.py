# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(my_word):
    enc = ""
    
    for char in my_word:
        if 97 <= ord(char) <= 123:
            enc += chr(219-ord(char))
        else:
            enc += char
    return enc
        
my_word = "Machine Learning"
print cipher(my_word)
print cipher(cipher(my_word))
