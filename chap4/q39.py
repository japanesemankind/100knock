#!/usr/bin/env python
# coding: utf-8

# In[28]:


from q30 import parse_mecab
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict 
import math

ans = defaultdict(int)
for sentence in parse_mecab():
    for morph in sentence:
        if morph['pos'] != '記号':
            ans[morph['base']] += 1
            
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
x_axis=list(range(1,len(ans)+1))
y_axis=[a[1] for a in ans]
plt.scatter(x_axis, y_axis)#1:90xx,2:80xx,...90xx:1のような組み合わせとなる
plt.xscale('log')
plt.yscale('log')
plt.show()


# In[ ]:




