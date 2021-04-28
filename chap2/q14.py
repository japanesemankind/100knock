#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
import sys
cmd1="cat popular-names.txt"
cmd2=f"head -n {sys.argv[1]}"
#catコマンドでファイルを表示し、ファイル内容をパイプに出力
file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
#前コマンドの出力を入力として受け取る
result=subprocess.run(cmd2.split(" "),text=True,input=file.stdout,stdout=subprocess.PIPE)
print(result.stdout)

