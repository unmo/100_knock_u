# -*- coding: utf-8 -*-

'''
72で抽出した素性を用いて、
ロジスティック回帰モデルを学習せよ．
'''
import argparse
import numpy as np
from train72 import get_feature
from sklearn.linear_model import LogisticRegression

def train_logistic_regression(features):
    
    features = np.array(features)    # 素性を持ったnumpy配列を作成。二次元配列。
    words = list(set(features[:,1]))    # 重複しているwordを削除する。python的。これはインデックスを指定して重複している数をカウントするため
    
    pos_vec = np.zeros(len(words))   # ポジティブベクトルの配列初期化
    neg_vec = np.zeros(len(words))   # ネガティブベクトルの配列初期化

    for feature in features:
        index = words.index(feature[1]) # indexメソッドで、対象の特徴語が、wordsリスト内のどの位置か調べる。
        if feature[0] == '-1':
            neg_vec[index] += 1         # pos_vecの指定のインデックスに、+1を加算
        else:
            pos_vec[index] += 1         # neg_vecの指定のインデックスに、+1を追加

    logit_model = LogisticRegression()  # 分類器のインスタンスを生成
    logit_model.fit([pos_vec, neg_vec],[1,-1]) # 訓練する。.fit(トレーニングベクトル,正解ベクトル)

    return (words,logit_model)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest = "sentiment", default = "sentiment.txt")
    args = parser.parse_args()
    #    logit = linear_model.LogisticRegression()
    features = get_feature(args.sentiment)
    train_logistic_regression(features)