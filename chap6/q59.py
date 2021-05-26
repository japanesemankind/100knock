#!/usr/bin/env python
# coding: utf-8

# In[2]:


#https://zenn.dev/yagiyuki/articles/0d6f97028fdd40209b7f
#https://qiita.com/FujiedaTaro/items/5784eda386146f1fd6e7
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
from sklearn.model_selection import RandomizedSearchCV

def load_data(filename):
    df=pd.read_table(filename,
                                   header=None,
                                   sep="\t",
                                   encoding="UTF-8")
    X=df.drop(df.columns[[len(df.columns)-1]], axis=1)#特徴量の取得
    Y=df[len(df.columns)-1]#ラベルの取得
    return X,Y

#データをロード
X_train,Y_train=load_data("train.feature.txt")
X_valid,Y_valid=load_data("valid.feature.txt")
X_test,Y_test=load_data("test.feature.txt")
hyper_param=np.logspace(-3, 3,num=7)

best_param=0
best_accuracy=0

for c in hyper_param:#10^(-3)~10^3までハイパーパラメータを変更
    
    lr = LogisticRegression(max_iter=1000,C=c)#ハイパーパラメータを指定して、インスタンスを作成
    lr.fit(X_train, Y_train)#重みを学習
    pred_valid=lr.predict(X_valid)
    accuracy=accuracy_score(Y_valid, pred_valid)

    if(best_accuracy < accuracy):#正解率が上がれば
        #最適パラメータを更新
        best_param=c
        best_accuracy=accuracy
        
lr = LogisticRegression(max_iter=1000,C=best_param)
lr.fit(X_train, Y_train)    
pred_test=lr.predict(X_test)
print(accuracy_score(Y_test, pred_test))


# In[ ]:




