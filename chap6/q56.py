#!/usr/bin/env python
# coding: utf-8

# In[1]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
import pickle
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
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
X_test,Y_test=load_data("test.feature.txt")

pred_test=lr.predict(X_test)
print(classification_report(Y_test, pred_test))

