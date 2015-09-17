# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ
"""
import argparse
from train_41 import chunks

def Verb_check(original_phrase) :
    if [morph.pos for morph in original_phrase.morphs if morph.pos == "動詞"]:
        return True
    else:
        return False

def Noun_check(destination_phrase) :
    if [morph.pos for morph in destination_phrase.morphs if morph.pos == "名詞"]:
        return True
    else:
        return False

def main(in_file):
    header = ["名詞","動詞"]
    print "\t".join(header)
    print "------------------"

    
    sentences = chunks(in_file)
    
    for sentence_number in range(len(sentences)):
        
        for phrase_number in range(len(sentences[sentence_number])):
            
            original_phrase = sentences[sentence_number][phrase_number]
            
            if Noun_check(original_phrase):
                destination_phrase = sentences[sentence_number][original_phrase.dst]
                if Verb_check(destination_phrase):
                    outputs = list()
                    outputs.append("".join( morph.surface for morph in original_phrase.morphs if not morph.pos == "記号"))
                    outputs.append("".join( morph.surface for morph in destination_phrase.morphs if not morph.pos == "記号"))
                    print "\t".join(outputs)

                else:
                    continue
            else:
                continue
                    
        
                
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="cabocha", default="neko.txt.cabocha", help="train_43 help")
    args = parser.parse_args()
    main(args.cabocha)
