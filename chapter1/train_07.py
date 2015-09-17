# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
def my_func(x,y,z):
    return "%s時の%sは%s" % (x,y,z)

if __name__ == '__main__' :
    x = 12
    y = "気温"
    z = 22.4
    print my_func(x,y,z)
    