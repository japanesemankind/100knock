#!/usr/bin/env python
# coding: utf-8

# In[8]:


from q41 import parse_q41
sentences=parse_q41()
sentence = sentences[2]
for chunk in sentence.chunks:
    #文節に名詞が含まれる場合
    if '名詞' in [morph.pos for morph in chunk.morphs]:
        
        #記号を除いて、文節をリストに追加
        leaf="".join(morph.surface for morph in chunk.morphs if morph.pos != '記号')
        path = [leaf]
        
        #根にたどり着く(根はdst=-1)まで
        while chunk.dst != -1:
            #文節をリストに追加
            path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs if morph.pos != '記号'))
            #かかり先文節に移動
            chunk = sentence.chunks[chunk.dst]
        #区切り文字を指定し、出力
        print(' -> '.join(path))

