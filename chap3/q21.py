#!/usr/bin/env python
# coding: utf-8

# In[11]:


import re
from q20 import q20 as article_extraction
def category_extraction():
    article=article_extraction()
    result="\n".join(re.findall("^\[\[Category:.*$",article,flags=re.MULTILINE))
    return result        
if __name__ == "__main__":
    print(category_extraction())


# In[ ]:




