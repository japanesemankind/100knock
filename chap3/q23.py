#!/usr/bin/env python
# coding: utf-8

# In[13]:


import re
from q20 import q20 as article_extraction

def section_name_extraction():
    result=""
    lines=article_extraction()
    list=re.findall("^(={2,})(.*?)(?:={2,})$",lines,flags=re.MULTILINE)
    #セクション名とレベルが組になったリストから、それぞれの要素を取り出して、resultに連結する
    result="\n".join(i[1]+":"+str(len(i[0])-1)  for i in list)
    return result
if __name__ == "__main__":
    print(section_name_extraction())


# In[ ]:




