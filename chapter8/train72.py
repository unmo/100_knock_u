# -*- coding: utf-8 -*-

'''
極性分析に有用そうな素性を各自で設計し，
学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''

import argparse
from train71 import check_stoplist
import re
import numpy
from stemming.porter2 import stem


def stemming(sentence):
        
    words = [stem(word.lower()) for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"\(\)]$", '', sentence.rstrip()).split()] 
    return words


def get_feature(in_file):

    features = []
    
    with open(in_file,"r") as sentiment_file:
        for line in sentiment_file:
            label = line[:2]
            for word in stemming(line[3:]):
                features.append([label,word])
                            
    return features  # 今回は簡単のため特徴量として各単語の頻出回数を使用する

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "sentiment", default = "sentiment.txt")
    args = parser.parse_args()
    
    features = get_feature(args.sentiment)

    print len([feature for feature in features if feature[0] == '-1'])
    print len([feature for feature in features if feature[0] == '+1'])


