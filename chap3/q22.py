#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
from q21 import category_extraction

def category_name_extraction():
    lines=category_extraction()
    #(パターン)で、グループ化とキャプチャを行う
    #(?:パターン)で、グループ化のみを行う
    result="\n".join(re.findall(r"^\[\[Category:(.*?)(?:\|.)?\]\]$",lines,flags=re.MULTILINE))
    return result
if __name__ == "__main__":
    print(category_name_extraction())


# In[ ]:




