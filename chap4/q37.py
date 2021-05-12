#!/usr/bin/env python
# coding: utf-8

# In[18]:


from q30 import parse_mecab
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict 
dic = defaultdict(int)

for sentence in parse_mecab():
    if "猫" in [morph["surface"] for morph in sentence]:  #文に「猫」が表層形で現れる場合だけ
        
        for morph in sentence:#形態素について
            if (morph["surface"]!="猫" and morph["pos"]!="記号"):
                dic[morph["base"]] += 1  # 出現回数(基本形)をカウント
                
dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
top_words=dic[0:10]
keys = [a[0] for a in top_words]
values = [a[1] for a in top_words]
plt.bar(keys, values)
plt.show()


# In[ ]:




