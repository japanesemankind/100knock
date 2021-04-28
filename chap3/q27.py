#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re
from q26 import remove_mackup_26
def remove_mackup_27():
    dictionary={}
    result=remove_mackup_26()
    for k,v in result.items():
        dictionary[k]=re.sub("\[\[(.+?)\|(.*?)\]\]","\\1\\2",v)
    return dictionary

if __name__ == "__main__":
    dic=remove_mackup_27()
    for i in dic:
        print(i+":   "+dic[i])


# In[ ]:




