#!/usr/bin/env python
# coding: utf-8

# In[1]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.metrics import accuracy_score
from q51_2 import load_data
#X_list:記事見出しのリスト
#Y_list:カテゴリ名のリスト
#def my_logistic_regression(X,Y,model):

lr=pickle.load(open("my_lr.model", 'rb'))

train_feature=load_data("train.feature.txt")
test_feature=load_data("test.feature.txt")
train=load_data("train.txt")
test=load_data("test.txt")
#学習データの取得
#train_df=pd.read_table("test.feature.txt",
#                                   header=None,
#                                   sep="\t",
#                                   encoding="UTF-8")
#X_train=train_df.drop(train_df.columns[[len(train_df.columns)-1]], axis=1)#特徴量の取得
#Y_test=train_df[len(train_df.columns)-1]#ラベルの取得

pred_train=lr.predict(train_feature)
pred_test=lr.predict(test_feature)
#print(pred_train)
#print(Y_train)
#print(pred_test)
#print(Y_test)
print(f"学習データでの正解率:{accuracy_score(train["CATEGORY"], pred_train)}")#学習データ上での正解率を表示
print(f"評価データでの正解率:{accuracy_score(test["CATEGORY"], pred_test)}")#評価データ上での正解率を表示


# In[ ]:




