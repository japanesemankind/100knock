#!/usr/bin/env python
# coding: utf-8

# In[6]:


def q5(lst,n):
    #結果(n-gram)を格納するリスト
    result=[]
    #1要素ずつ,後にn要素取れなくなるまでループを行う
    for idx in range(0,len(lst)-n+1):
        #idxからn要素を取り出し,結果に格納する
        result.append(lst[idx:idx+n])
    return result

sentence="I am an NLPer"

#文字bi-gram
print(q5(sentence,2))
#単語bi-gram
print(q5(sentence.split(),2))

