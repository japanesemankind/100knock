#!/usr/bin/env python
# coding: utf-8

# In[5]:


from q30 import parse_mecab
from collections import defaultdict 

def count_words():
    sentences=parse_mecab()
    ans = defaultdict(int)#初期値0の辞書
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] != '記号':
                ans[morpheme["base"]] += 1#出現回数を加算
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)#x[0]にキー,x[1]に値が入る
    return ans
# 確認
if __name__=="__main__":
    dic=count_words()
    for i in dic[:20]:
        print(i)

