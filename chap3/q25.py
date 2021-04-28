#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from q20 import q20 as article_extraction
def templates_extraction():
    dictionary={}
    article=article_extraction()
    pattern = "^\{\{基礎情報.*$([\s\S]*?)^\}\}$"
    basic_info = "\n".join(re.findall(pattern,article,flags=re.MULTILINE))
    #行頭の"|"から先のフィールド名をキャプチャし、空白と"="の後に続く値をキャプチャする
    
    #公式国名について、値に"\n"が含まれる。そのためre.DOTALLを用いて、.が"¥n"にもマッチするようにする
    #また、テンプレートの区切りを、"\n"だけでなく、その次に、次のテンプレートの行頭がくるかで判断する
    pattern="^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))"
    result=re.findall(pattern,basic_info,flags=re.MULTILINE+re.DOTALL)
    
    #re.findall()の戻り値となるリストは直接辞書に代入できない？
    for i,k in result:
        dictionary[i]=k
    return dictionary
if __name__ == "__main__":
    tmp=templates_extraction()
    for i in tmp:
        print(i+":"+tmp[i]+"\n")


# In[ ]:




