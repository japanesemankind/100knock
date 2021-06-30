#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from scipy.stats import spearmanr
from gensim.models import KeyedVectors
import pandas as pd

model=KeyedVectors.load('q60_model.pt', mmap='r')

# df = pd.read_table("combined.csv",
#                                    header=0,#ヘッダとして0行目を指定
# #                                   names=("ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIME"),
#                                    sep=",",
#                                    encoding="UTF-8")
# #print(df)
# df_sorted=df.sort_values(by=["Word1","Human(mean)"],ascending=[True,False])
# print(df_sorted)
# df_sorted.to_csv("combined_q66.csv", sep=",",index=False)

df = pd.read_table("combined_q66.csv",#各Word1ごとに、Human(mean)の値でソートしたファイル
                                   header=0,#ヘッダとして0行目を指定
                                   sep=",",
                                   encoding="UTF-8")

target_word="computer"

df_word=df[df['Word1']==target_word]#
list_human=list(range(1,len(df_word)+1))#ソート済みのファイルを利用しているため、rangeで連番のリストを作成する

#各Word2について、類似度を計算
df_model=pd.DataFrame([[model.similarity(target_word,word2) for word2 in df_word["Word2"].values.tolist()]]).T[0]
#類似度順にソート
df_model_sorted=df_model.sort_values(0,ascending=False)
#順位に+1して、リストに出力
list_model=list([rank+1 for rank in df_model_sorted.index])

print(f"目的の単語{target_word}")
print(f"スピアマンの順位相関係数:{spearmanr(list_human,list_model)[0]}")


# In[ ]:




