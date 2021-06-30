#!/usr/bin/env python
# coding: utf-8

# In[10]:


from q30 import parse_mecab

ans = set()#重複を無視するため、集合型に抽出
sentences=parse_mecab()
for sentence in sentences:
    juncture = ''
    n = 0
    
    for morph in sentence:
        if morph['pos'] == '名詞': #連接(juncture)に連結
            juncture = ''.join([juncture, morph['surface']])#連接(juncture)に連結
            n+=1
            
        else:#名詞以外の場合
            if(n>=2):#名詞の連接が出現している(n>2)場合
                ans.add(juncture)
            #初期化
            juncture = ''
            n=0
            
            
    if n>=2:#文末に出てくる名詞の連接は別処理
        ans.add(juncture)
            
# 確認
print(f"種類: {len(ans)}\n")
for i in range(30):
    print(ans.pop())

