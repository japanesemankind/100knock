#!/usr/bin/env python
# coding: utf-8

# In[10]:


def q2(str_A,str_B):
    #zip(),forを用いて2つの入力文字列から1文字ずつ取り出す.その後join()を用いて,取り出した文字を連結する.
    return ''.join([char_A+char_B for char_A,char_B in zip(str_A,str_B)])
print(q2("パトカー","タクシー"))


# In[ ]:




