#!/usr/bin/env python
# coding: utf-8

# In[3]:


import subprocess
cmd1="cat popular-names.txt"
cmd2="sort -k 3 -n -r"
file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
result=subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=subprocess.PIPE)
print(result.stdout)

