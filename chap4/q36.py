#!/usr/bin/env python
# coding: utf-8

# In[15]:


from q35 import count_words
import matplotlib.pyplot as plt
import japanize_matplotlib
dic=count_words()
top_words=dic[0:10]
keys = [a[0] for a in top_words]
values = [a[1] for a in top_words]
plt.bar(keys, values)
plt.show()

