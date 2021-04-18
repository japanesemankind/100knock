#!/usr/bin/env python
# coding: utf-8

# In[20]:


import re
def q3(str_arg):
    words=re.sub(r',|\.','',str_arg).split()
    #リストの置換方法は,インデックス指定か、リスト内包表記を用いる
    return [len(word) for word in words]
print(q3("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))

