# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""
import argparse
from stemming.porter2 import stem
#from sklearn.feature_extraction.text import TfidfVectorizer

def stopword(sentiment):
    
    stop_list = list()
    feature_list = list()
    label_list = list()
    
    """
    ストップワード、その他不要文字の削除
    """
    with open("stopwords.txt","r") as stop_file:
        for stop_word in stop_file:
            stop_word = stop_word.rstrip("\n")
            stop_list.append(stop_word)
    
    with open(sentiment,"r") as sentiment_text:
       # ストップワード等の削除

        for text in sentiment_text:
            text = text.strip()
            sp = text.split(" ")
            label = sp[0]
            message = sp[1:]
            features = []
            
            label_list.append(label)
            
            # messageリスト内のストップワード、カンマ、ピリオド
            for word in message[:]:
                if word in stop_list:
                    message.remove(word)
                elif word == "," or word == "." or word == "-" or word ==  "(" or word == ")" or word == "--" or word == "---" or word == "!" or word == "?" or word == '"' or word == "'" or word == ";" or word == ":" or word == "" :
                    message.remove(word)
                else:
                    pass
            features += [stem(w) for w in message]               
            
            text = " ".join([label] + features)
            feature_list.append(text)
            
        for line in feature_list:
            print line
                                    
        
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "sentiment", default = "sentiment.txt", help = "sentiment_file")
    args = parser.parse_args()
    stopword(args.sentiment)
    
