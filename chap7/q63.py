#!/usr/bin/env python
# coding: utf-8

# In[3]:


from gensim.models import KeyedVectors

#オプションmmapで、ディスクからの読み込みを高速化?
#公式ドキュメント:https://radimrehurek.com/gensim/models/keyedvectors.html
model=KeyedVectors.load('q60_model.pt', mmap='r')
positive=["Spain", "Athens"]
negative=["Madrid"]
print(f"{positive}-{negative}の余弦類似度ランク")
print(model.most_similar(positive, negative, topn=10))#most_simmilar:余弦類似度の高い単語から順に、topn個出力


# In[ ]:




