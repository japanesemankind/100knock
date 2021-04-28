#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
cmd1="cat popular-names.txt"
cmd2="cut -f 1"
cmd3="cut -f 2"

file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)

#出力先をファイルに指定
with open("col1.txt","w") as col1:
    subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=col1)
#出力先をファイルに指定    
with open("col2.txt","w") as col2:
    subprocess.run(cmd3.split(" "),text=True,input=file.stdout,stdout=col2)


# In[ ]:




