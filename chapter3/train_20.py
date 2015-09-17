# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
/1行に1記事の情報がJSON形式で格納される
/各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
/ファイル全体はgzipで圧縮される
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
import sys
import json

with open(sys.argv[1],"r") as read_file, open(sys.argv[2],"w") as write_file:
    for line in read_file:
        line = line.strip()
        data = json.loads(line)
        if data["title"] == u"イギリス":
            write_file.write(data["text"].encode("utf-8"))


