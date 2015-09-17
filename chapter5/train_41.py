# -*- coding: utf-8 -*-
"""
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import argparse
from train_40 import Morph


class Chunk:
    def __init__(self, phrase_number, phrases, relations):
        self.morphs = [Morph(line) for line in phrases[phrase_number]]
        self.dst = relations[phrase_number][-1]
        self.srcs = [source for source, destination in relations if destination == phrase_number]
        if not self.srcs:
            self.srcs = [-1]


def renew_phrase(phrase, phrases):
    if phrase:
        phrases.append(phrase)
        phrase = list()
    return phrase, phrases


def chunks(in_file):
    with open(in_file,"r") as fin:
        phrase = list()
        phrases = list()
        relations = list()
        sentences = list()

        for line in fin:
            if line.startswith("* "):
                phrase, phrases = renew_phrase(phrase, phrases)
                relations.append(tuple([int(number.replace("D", "")) for number in line.strip().split(" ")[1:3]]))                
            elif line == "EOS\n":                
                phrase, phrases = renew_phrase(phrase, phrases)
                sentences.append([Chunk(phrase_number, phrases, relations) for phrase_number in range(len(relations))])                
                phrases = list()
                relations = list()
            else:
                phrase.append(line)
    return sentences

def main(in_file):
    sentences = chunks(in_file)

    for phrase_number, phrase in enumerate(sentences[8]):
        
        print phrase_number, ": " + " ".join([morph.surface for morph in phrase.morphs]) + "\tdst:" + str(phrase.dst) + "\tsrc:" + ",".join([str(source) for source in phrase.srcs])

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="cabocha", default="neko.txt.cabocha", help="train_40 help")
    args = parser.parse_args()
    main(args.cabocha)
    
        
        
