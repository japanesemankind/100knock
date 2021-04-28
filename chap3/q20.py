#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
def q20():
    filename="jawiki-country.json"
    with open (filename,"r") as f:
        for line in f:
            article=json.loads(line)
            if(article["title"]=="イギリス"):
                return article["text"]
            
if __name__ == "__main__":
    print(q20())


# In[ ]:




