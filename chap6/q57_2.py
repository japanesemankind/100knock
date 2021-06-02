#!/usr/bin/env python
# coding: utf-8

# In[7]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
import pickle
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from q51_2 import load_data
#X_list:記事見出しのリスト
#Y_list:カテゴリ名のリスト
#def my_logistic_regression(X,Y,model):
lr=pickle.load(open("my_lr.model", 'rb'))
#df=pd.read_table("tmp.txt",#評価データにヘッダを付けたもの
#                                   sep="\t",
#                                   encoding="UTF-8")
#print(df.columns)

df=load_data("test.feature.txt")

#クラス名と特徴量を取得
for cl,coef in zip(lr.classes_,lr.coef_):
#    print(len(coef))
#    print(len(df.columns))
#    print(coef)
    sorted_index=coef.argsort()
    print(f"class:{cl}")
    for i in range (0,10):
        print(f"下位{i+1}:"+df.columns[sorted_index[i]]+f",{coef[sorted_index[i]]}")
    print()
    
    for i in range (0,10):
        print(f"上位{i+1}:"+df.columns[sorted_index[-i-1]]+f",{coef[sorted_index[-i-1]]}")    
    print()


# In[ ]:




