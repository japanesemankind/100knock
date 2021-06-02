#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from gensim.models import KeyedVectors
from q67 import country_load_q67

#model=KeyedVectors.load('q60_model.pt', mmap='r')

#with open("my_country_list_mini.csv","r") as f:
    #country_names=[line.split(sep=",")[1] for line in f if line.split(sep=",")[1] in model]#モデル内に存在する国名だけ、リストに追加
    #word_vec=[model[country] for country in country_names]#単語ベクトルを取り出す
    
country_names,word_vec=country_load_q67("my_country_list_20.csv")
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
Z = linkage(word_vec, method='ward',metric="euclidean")#ward法、ユークリッド距離で階層型クラスタリング
dendrogram(Z, labels=country_names)
plt.xticks(rotation=90)
plt.figure(figsize=(15, 5))
plt.show()


# In[ ]:




