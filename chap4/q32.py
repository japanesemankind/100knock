#!/usr/bin/env python
# coding: utf-8

# In[1]:


from q30 import parse_mecab

ans = set()#重複を無視するため、集合型に抽出
sentences=parse_mecab()

for sentence in sentences:
    for morph in sentence:
        
        if morph["pos"] == '動詞':
            ans.add(morph["base"]) #集合に追加
            
# 確認
print(f"種類: {len(ans)}\n")

for i in range(10):
    print(ans.pop())

