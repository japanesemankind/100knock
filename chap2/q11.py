#!/usr/bin/env python
# coding: utf-8

# In[68]:


import subprocess
cmd1="cat popular-names.txt"
#catコマンドでファイルを表示し、ファイル内容をパイプに出力
file=subprocess.run(cmd1.split(" "),text=True,stdout=subprocess.PIPE)
#split()は、置換先の空白でも分割してしまうため、使用しない
result=subprocess.run(["tr","\t"," "],text=True,input=file.stdout,stdout=subprocess.PIPE)
print(result.stdout)


# In[ ]:




