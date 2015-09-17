# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
import train_30
import argparse
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='C:\Windows\Fonts\msgothic.ttc')

def count_ten(neko_dict):
    count_list = list()
    most_ten_word = list()
    most_ten_count = list()


    for neko_list in neko_dict:
        for m in neko_list:
            count_list.append(m["surface"])
            
    for words,count in Counter(count_list).most_common(1000):
        most_ten_word.append(words)   
        most_ten_count.append(count)
        
    return (most_ten_word,most_ten_count)
      
def graph_plot(word_ten,count_ten):
    
    kind_count = list()
    
    for kind in count_ten:
        kind_count.append(count_ten.count(kind))
    
    plt.title(u"Zipfの定理", fontdict = {"fontproperties": fp})
    plt.xlabel(u"順位", fontdict = {"fontproperties": fp})
    plt.ylabel(u"出現頻度", fontdict = {"fontproperties": fp})
        
    X = list()
    
    for i in range(0,1000):
        X.append(i)
        
    plt.xscale("log")
    plt.yscale("log")
    
    plt.plot(X,count_ten,"ro")
    
    
   
if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser()
    parser.add_argument( "-i", "--input", dest = "input_file" ,default = "neko.mecab", help = "train_37 help" )
    args = parser.parse_args();
    morph = train_30.morph(args.input_file)
    most_ten_word,most_ten_count = count_ten(morph)
    graph_plot(most_ten_word,most_ten_count)

