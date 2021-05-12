#!/usr/bin/env python
# coding: utf-8

# In[29]:


from q30 import parse_mecab
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict 
dic = defaultdict(int)

for sentence in parse_mecab():        
        for morph in sentence:#形態素について
            if (morph["pos"]!="記号"):
                dic[morph["base"]] += 1  # 出現回数(基本形)をカウント
word_count=list(dic.values())
print(type(word_count))
#plt.hist(word_count,bins=max(word_count),range=(1,40))#出現回数について、階級は1,2,...~最大出現回数
plt.hist(word_count,bins=100)#問題に沿う形にすると、グラフが見えなかったため、このような形とした
plt.xlim(xmin=1, xmax=max(word_count))#最大出現回数まで表示
plt.show()


# In[ ]:




