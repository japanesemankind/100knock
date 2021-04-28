#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re
from q20 import q20 as article_extraction
def category_extraction():
    article=article_extraction()
    #[[ファイル:ファイル名|その他情報の並びにマッチし、ファイル名だけを返す
    pattern = "\[\[ファイル:(.+?)\|"
    result = "\n".join(re.findall(pattern,article))
    return result

print(category_extraction())


# In[ ]:




