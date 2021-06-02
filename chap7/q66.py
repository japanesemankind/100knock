#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import spearmanr
from gensim.models import KeyedVectors

model=KeyedVectors.load('q60_model.pt', mmap='r')

list_human=[]
list_model=[]
with open("combined.csv","r") as f:
    for id,line in enumerate(f):
        
        #ヘッダを読み飛ばす
        if(id==0):
            continue
        
        line=line.split(sep=",")
        list_human.append(line[2])
        list_model.append(model.similarity(line[0], line[1]))
#list1=[1,2,3,4,5]
#list2=[1,2,4,3,5]
#list3=[1.5,2.3,3.4,4.6,5.7]
#list4=[1.5,2.3,4.6,3.4,5.7]
print(f"スピアマンの順位相関係数:{spearmanr(list_human,list_model)[0]}")
#print(spearmanr(list1,list2))
#print(spearmanr(list3,list4))

