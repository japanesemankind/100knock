#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def q4(str_arg):
    dict={}
    one_char=[0,4,5,6,7,8,14,15,18]
    words=re.sub(r',|\.','',str_arg).split()
    
    for idx,word in enumerate(words):
        if(idx in one_char):
            words[idx]=word[0:1]
        else:
            words[idx]=word[0:2]
        dict[words[idx]]=idx
    return dict
print(q4("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"))


# In[ ]:




