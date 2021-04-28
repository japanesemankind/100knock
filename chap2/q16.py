#!/usr/bin/env python
# coding: utf-8

# In[14]:


import subprocess
import sys
cmd1="cat popular-names.txt"
cmd2="wc -l"
file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
line_number=subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=subprocess.PIPE)
split_number=round(int(line_number.stdout)/int(sys.argv[1]))
#split_number=round(int(line_number.stdout)/2)
#print(split_number)
cmd3=f"split -l {split_number}"
#cmd3="split -l 200"
result=subprocess.run(cmd3.split(" "),text=True,input=file.stdout)

