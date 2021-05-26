#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
train_df=pd.read_table("train.feature.txt",
                                   header=None,
                                   sep="\t",
                                   encoding="UTF-8")
#print(train_df)
#print(len(train_df.columns))
#print(train_df[len(train_df.columns)-1])
X_train=train_df.drop(train_df.columns[[90]], axis=1)
Y_train=train_df[len(train_df.columns)-1]#特徴量を取得
#X_train=train_df[0:len(train_df.columns)-2]#カテゴリ名を取得
#print(X_train)
#print(train_df.iloc[train_df.columns-1:train_df.columns])
print(X_train)
print(Y_train)
lr = LogisticRegression(max_iter=1000)#インスタンスを作成、デフォルトで収束しなかったため1000とした
lr.fit(X_train, Y_train)#重みを学習

#モデルをシリアライズして保存
filename="my_lr.model"
pickle.dump(lr, open(filename, 'wb'))


# In[ ]:




