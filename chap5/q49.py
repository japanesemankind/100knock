#!/usr/bin/env python
# coding: utf-8

# In[19]:


from itertools import combinations
from q41 import parse_q41
import re
sentences=parse_q41()
sentence = sentences[2]
nouns = []
for i, chunk in enumerate(sentence.chunks):
    #名詞を含む文節であれば

    if '名詞' in [morph.pos for morph in chunk.morphs]:
        #文節インデックスのリストに追加
        nouns.append(i)
    
    #文節インデックスから2個選ぶ組のすべてについて
    for i, j in combinations(nouns, 2):
        
        #パスを作成
        path_i = []
        path_j = []
        
        #i,jが共通の文節に来るまで
        while i != j:
            if i < j:
                path_i.append(i)
                i = sentence.chunks[i].dst
                
            else:
                path_j.append(j)
                j = sentence.chunks[j].dst
                
            if len(path_j) == 0:  # 1つ目のケース
                
                #各形態素について、名詞であればXに変換して、pathに追加
                #名詞でなければ、そのままpathに追加
                chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
                chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[i].morphs])
                
                #名詞の連接をX、Yに変換
                chunk_X = re.sub('X+', 'X', chunk_X)
                chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                #開始文節:chunk_X
                #path_i(通る文節のインデックス)を用いて、始まりのchunk_Xを除いて文節を読みとり、文字列に変換
                #終了文節:chunk_Y
                path_XtoY = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]] + [chunk_Y]
                
                #区切り文字を指定して出力
                print(' -> '.join(path_XtoY))
                
            else:  # 2つ目のケース
                chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
                chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[path_j[0]].morphs])
                
                #共通の文節のインデックスはiで表される(whileで共通の文節に来るまでループしている)
                chunk_k = ''.join([morph.surface for morph in sentence.chunks[i].morphs])

                chunk_X = re.sub('X+', 'X', chunk_X)
                chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                
                path_X = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]]
                path_Y = [chunk_Y] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_j[1:]]
                
#                print(" -> ".join(path_X))
#                print(" -> ".join(path_Y))
                X_tmp=" -> ".join(path_X)
                Y_tmp=" -> ".join(path_Y)
#                print(chunk_k)
                result="|".join([X_tmp,Y_tmp,chunk_k])
                print(result)
#                print("|".join(X_tmp,Y_tmp))
                #print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k])


# In[ ]:




