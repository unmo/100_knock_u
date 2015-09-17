# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015
@author: umezawa
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

"""
import random
import argparse

def make_sentiment(pos_file,neg_file):
    
    pos_list = list()
    neg_list = list()
    text_list = list()
    pos_count = 0
    neg_count = 0
    
    with open(pos_file,"r") as pos:
        for line in pos:
            pos_line = (" ").join(["+1",line])
            pos_list.append(pos_line)
            
    with open(neg_file,"r") as neg:
        for line in neg:
            neg_line = (" ").join(["-1",line])
            neg_list.append(neg_line)
            
    text_list = pos_list + neg_list
    random.shuffle(text_list)
    
    for text in text_list:
        print text.rstrip("\n")
        if text.startswith("+"):
            pos_count += 1
        else:
            neg_count += 1
        
#    print "pos_count:%s  , neg_count:%s" % (pos_count,neg_count)
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--positive", dest = "pos_file", default = "rt-polarity.pos", help = "positive file")
    parser.add_argument("-n", "--negative", dest = "neg_file", default = "rt-polarity.neg", help = "negative_file")
    args = parser.parse_args()
    make_sentiment(args.pos_file,args.neg_file)
    


