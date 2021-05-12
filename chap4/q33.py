#!/usr/bin/env python
# coding: utf-8

# In[19]:


from q30 import parse_mecab

ans = set()#重複を無視するため、集合型に抽出
sentences=parse_mecab()
for sentence in sentences:
    for i in range(1, len(sentence) - 1):# 最後から2文字まで(リストのインデックスを超えないため)
        if sentence[i - 1]['pos'] == '名詞' and sentence[i]['surface'] == 'の' and sentence[i + 1]['pos'] == '名詞':
            ans.add(sentence[i - 1]['surface'] + sentence[i]['surface'] + sentence[i + 1]['surface'])
            
# 確認
print(f"種類: {len(ans)}\n")

for i in range(10):
    print(ans.pop())


# In[ ]:




