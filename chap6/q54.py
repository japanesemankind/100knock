#!/usr/bin/env python
# coding: utf-8

# In[5]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.metrics import accuracy_score
#X_list:記事見出しのリスト
#Y_list:カテゴリ名のリスト
#def my_logistic_regression(X,Y,model):
    
def load_data(filename):
    df=pd.read_table(filename,
                                   header=None,
                                   sep="\t",
                                   encoding="UTF-8")
    X=df.drop(df.columns[[len(df.columns)-1]], axis=1)#特徴量の取得
    Y=df[len(df.columns)-1]#ラベルの取得
    return X,Y

lr=pickle.load(open("my_lr.model", 'rb'))

X_train,Y_train=load_data("train.feature.txt")
X_test,Y_test=load_data("test.feature.txt")
#学習データの取得
#train_df=pd.read_table("test.feature.txt",
#                                   header=None,
#                                   sep="\t",
#                                   encoding="UTF-8")
#X_train=train_df.drop(train_df.columns[[len(train_df.columns)-1]], axis=1)#特徴量の取得
#Y_test=train_df[len(train_df.columns)-1]#ラベルの取得

pred_train=lr.predict(X_train)
pred_test=lr.predict(X_test)
#print(pred_train)
#print(Y_train)
#print(pred_test)
#print(Y_test)
print(accuracy_score(Y_train, pred_train))#学習データ上での正解率を表示
print(accuracy_score(Y_test, pred_test))#評価データ上での正解率を表示


# In[ ]:




