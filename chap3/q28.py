#!/usr/bin/env python
# coding: utf-8

# In[13]:


import re
from q27 import remove_mackup_27
def remove_mackup():
    dictionary={}
    for k,v in remove_mackup_27().items():
        
        #htmlタグの除去
        dictionary[k]=re.sub("<(.+?)>","",v)
        
        #ファイルリンクの除去
        dictionary[k]=re.sub("\{\{(.+?)\|ファイル:(.+?)\}\}","\\1\\2",dictionary[k])
        
        #"{{    }}""の形のマークアップを除去
        dictionary[k]=re.sub("{{(.+?)}}","\\1",dictionary[k])
        #k=re.sub("\{\{(.+?)\}\}","\\1",k)
    return dictionary

if __name__ == "__main__":
    dic=remove_mackup()
    for i in dic:
        print(i+":   "+dic[i])


# In[ ]:




