# -*- coding: utf-8 -*-

'''
74.
73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
75.
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
76.
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
77.
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

'''
import argparse
import numpy as np
from train72 import get_feature, stemming
from train73 import train_logistic_regression
import sklearn.cross_validation as crv
from sklearn import linear_model

tp = 0
tn = 0
fp = 0
fn = 0

def verification(label,predict):

    if label == predict and predict == 1 :
        global tp
        tp += 1
    elif label == predict and predict == -1 :
        global tn
        tn += 1
    elif label != predict and predict == 1 :
        global fp
        fp += 1
    elif label != predict and predict == -1 :
        global fn
        fn += 1
    else:
        print "error"
        exit()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "sentiment", default = "sentiment.txt")
    parser.add_argument("-v", "--verification", dest = "verification", default = "test_data.txt")
    args = parser.parse_args()
    
    features = get_feature(args.sentiment) # 学習要データの素性生成
    features = np.array(features)          # 素性を持ったnumpy配列を作成。二次元配列。

# クロス    
#    train_data, test_data, train_target, test_target = crv.train_test_split(features[:,1], features[:,0], test_size = 0.2 ,random_state = 0 )    
#    train = np.c_[train_target, train_data]
#    verification = np.c_[test_target,test_data]

# ロジスティック回帰モデルの作成
# 戻り値は単語とモデル        
    logistic_model_instance = train_logistic_regression(features)
    words = logistic_model_instance[0]
    logit_model = logistic_model_instance[1]

# 入力データとして1割       
    with open(args.verification) as verification_file:
        for sentence in verification_file:
            label = sentence[:2]
            sentence = sentence[3:]
            input_vec = np.zeros(len(words))
            
            for word in stemming(sentence):
                try:
                    index = words.index(word)
                    input_vec[index] += 1
                except:
                    continue
                
            print "正解ラベル: ", int(label) , "予測ラベル: ", int(logit_model.predict(input_vec)) , "予測確率: " , logit_model.predict_proba(input_vec)
            
            verification( int(label),int(logit_model.predict(input_vec)) )
        
        accuracy = float(tp+tn)/(tp+tn+fn+fp)
        precision = float(tp)/(tp+fp)
        recall = float(tp)/(tp+fn)
        f = float((2*recall*precision))/(recall+precision)
        print 'Accuracy %f, precision %f, recall %f, F1 %f ' % (accuracy, precision, recall, f)
        
    


