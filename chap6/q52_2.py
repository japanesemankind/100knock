#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from q51_2 import load_data
import pickle
train_feature=load_data("train.feature.txt")
train=load_data("train.txt")
#print(train_df)
#print(len(train_df.columns))
#print(train_df[len(train_df.columns)-1])
#X_train=train_df[0:len(train_df.columns)-2]#カテゴリ名を取得
#print(X_train)
#print(train_df.iloc[train_df.columns-1:train_df.columns])
#print(train_feature)
#print(train)
lr = LogisticRegression(max_iter=1000)#インスタンスを作成、デフォルトで収束しなかったため1000とした
lr.fit(train_feature, train["CATEGORY"])#重みを学習

#モデルをシリアライズして保存
filename="my_lr.model"
pickle.dump(lr, open(filename, 'wb'))


# In[ ]:




