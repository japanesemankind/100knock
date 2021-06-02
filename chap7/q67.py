#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
from gensim.models import KeyedVectors
import numpy as np


def country_load_q67(filename):
    
    model=KeyedVectors.load('q60_model.pt', mmap='r')
    
    with open(filename,"r") as f:
        country_names=[line.split(sep=",")[1] for line in f if line.split(sep=",")[1] in model]#モデル内に存在する国名だけ、リストに追加
        word_vec=[model[country] for country in country_names]#リストから単語ベクトルを取り出す
    return country_names,word_vec

if __name__=="__main__":
    labels,vectors=country_load_q67("my_country_list.csv")
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(vectors)
#    print(kmeans.labels_)
    for i in range(5):
        cluster = np.where(kmeans.labels_ == i)[0]#ラベルがiのデータ(インデックス)だけ抽出
        print('cluster', i)
        print(', '.join([labels[k] for k in cluster]))#クラスタ内の各データ(インデックス)について、国名を表示


# In[ ]:




