#!/usr/bin/env python
# coding: utf-8

# In[3]:


from gensim.models import KeyedVectors

#オプションmmapで、ディスクからの読み込みを高速化?
#公式ドキュメント:https://radimrehurek.com/gensim/models/keyedvectors.html
model=KeyedVectors.load('q60_model.pt', mmap='r')
word1="United_States"
word2="U.S."
print(f"「{word1}」と「{word2}」の余弦類似度:{model.similarity(word1, word2)}")#similarity:余弦類似度を計算

