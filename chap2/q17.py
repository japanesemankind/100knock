#!/usr/bin/env python
# coding: utf-8

# In[2]:


import subprocess
cmd1="cat popular-names.txt"
cmd2="cut -f 1"
cmd3="sort"
cmd4="uniq -d"

file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
col1=subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=subprocess.PIPE)
sort=subprocess.run(cmd3.split(" "),text=True,input=col1.stdout,stdout=subprocess.PIPE)
result=subprocess.run(cmd4.split(" "),text=True,input=sort.stdout,stdout=subprocess.PIPE)
print(result.stdout)


# In[ ]:




