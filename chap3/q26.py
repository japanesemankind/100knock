#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from q25 import templates_extraction
def remove_mackup_26():
    dic={}
    templates=templates_extraction()
    for k,v in templates.items():
        dic[k]=re.sub("\'{2,5}'","",v)
    return dic
if __name__ == "__main__":
    dic=remove_mackup_26()
    for i in dic:
        print(i+":"+dic[i]+"\n")
     

