#!/usr/bin/env python
# coding: utf-8

# In[7]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
#X_list:記事見出しのリスト
#Y_list:カテゴリ名のリスト
#def my_logistic_regression(X,Y,model):
    

    
lr=pickle.load(open("my_lr.model", 'rb'))
valid_df=pd.read_table("valid.feature.txt",
                                   header=None,
                                   sep="\t",
                                   encoding="UTF-8")
X_valid=valid_df.drop(valid_df.columns[[len(valid_df.columns)-1]], axis=1)
Y_valid=valid_df[len(valid_df.columns)-1]
Y_pred=lr.predict(X_valid)

Y_pred_proba=lr.predict_proba(X_valid)#クラス0~3に属する確率のリスト
print(Y_pred)
print(Y_pred_proba)


# In[ ]:




