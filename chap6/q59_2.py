#!/usr/bin/env python
# coding: utf-8

# In[3]:


#https://zenn.dev/yagiyuki/articles/0d6f97028fdd40209b7f
#https://qiita.com/FujiedaTaro/items/5784eda386146f1fd6e7
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from q51_2 import load_data


#データをロード
X_train=load_data("train.feature.txt")
X_valid=load_data("valid.feature.txt")
X_test=load_data("test.feature.txt")
Y_train=load_data("train.txt")["CATEGORY"]
Y_valid=load_data("valid.txt")["CATEGORY"]
Y_test=load_data("test.txt")["CATEGORY"]
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
        
lr = LogisticRegression(max_iter=2000,C=best_param)
lr.fit(X_train, Y_train)
pred_test=lr.predict(X_test)
print(f"最適パラメータ:{best_param}")
print(f"最高正解率:{accuracy_score(Y_test, pred_test)}")


# In[ ]:




