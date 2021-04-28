#!/usr/bin/env python
# coding: utf-8

# In[2]:


import subprocess
import sys
cmd1="cat popular-names.txt"
cmd2="cut -f 1"
cmd3="sort"
cmd4="uniq -c"
cmd5="sort -n -r"
#catコマンドでファイルを表示し、ファイル内容をパイプに出力
file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
#前コマンドの出力を入力として受け取る
col1=subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=subprocess.PIPE)
col1_sort=subprocess.run(cmd3.split(" "),text=True,input=col1.stdout,stdout=subprocess.PIPE)
uniq=subprocess.run(cmd4.split(" "),text=True,input=col1_sort.stdout,stdout=subprocess.PIPE)
result=subprocess.run(cmd5.split(" "),text=True,input=uniq.stdout,stdout=subprocess.PIPE)
print(result.stdout)

