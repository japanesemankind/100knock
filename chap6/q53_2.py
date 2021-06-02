#!/usr/bin/env python
# coding: utf-8

# In[1]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from q51_2 import load_data
import pickle
#X_list:記事見出しのリスト
#Y_list:カテゴリ名のリスト
#def my_logistic_regression(X,Y,model):
    

    
lr=pickle.load(open("my_lr.model", 'rb'))
test_feature=load_data("test.feature.txt")
test=load_data("test.txt")
Y_pred=lr.predict(test_feature)

Y_pred_proba=lr.predict_proba(test_feature)#クラス0~3に属する確率のリスト
print(Y_pred)
print(Y_pred_proba)


# In[ ]:




