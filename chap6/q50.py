#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn.model_selection import train_test_split
#カンマ区切りはread_csv()、タブ区切りはread_tabel()を使用
df = pd.read_table("newsCorpora.csv",
                                   header=None,
                                   names=("ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIME"),
                                   sep="\t",
                                   encoding="UTF-8")
instance=df.query("PUBLISHER in ['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail']")
instance_loc=instance.loc[:,["CATEGORY","TITLE"]]
#print(instance)
train,valid=train_test_split(instance_loc,test_size=0.20)#訓練データと検証データに分割
valid,test=train_test_split(valid,test_size=0.25)#検証データを、検証データと評価データに再分割

#余分なものをつけずに出力
train.to_csv("train.txt", sep="\t",header=False,index=False)
valid.to_csv("valid.txt", sep="\t",header=False,index=False)
test.to_csv("test.txt", sep="\t",header=False,index=False)

#print(valid)
#print(df.query("PUBLISHER in ['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail']"))
#ID タイトル URL 情報元 カテゴリ  ストーリー URLホスト名 日付


# In[ ]:




