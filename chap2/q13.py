#!/usr/bin/env python
# coding: utf-8

# In[2]:


import subprocess
cmd="paste col1.txt col2.txt"

with open("col.txt","w") as col:
    result=subprocess.run(cmd.split(" "),text=True,stdout=col)


# In[ ]:




