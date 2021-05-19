#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cat q47.txt | cut -f 1 | sort | uniq -c | sort -nr | head -n 3
#cat q47.txt | cut -f 1,2 | sort | uniq -c | sort -nr | head -n 3
from q41 import parse_q41
sentences=parse_q41()
with open("q47.txt", "w") as f:
    for sentence in sentences:
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                #動詞であれば
                if morph.pos == '動詞':
                    
                    for i, src in enumerate(chunk.srcs):
                        #サ変接続+をの形になっていれば
                        if len(sentence.chunks[src].morphs) == 2 and sentence.chunks[src].morphs[0].pos1 == 'サ変接続' and sentence.chunks[src].morphs[1].surface == 'を':
                            #述語(サ変接続+を)を取り出す
                            predicate = ''.join([sentence.chunks[src].morphs[0].surface, sentence.chunks[src].morphs[1].surface, morph.base])
                            cases = []
                            modi_chunks = []
                            #残りのかかり元文節から、助詞を探す
                            for src_r in chunk.srcs[:i] + chunk.srcs[i + 1:]:  # 残りの係り元chunkから助詞を探す
                                case = [morph.surface for morph in sentence.chunks[src_r].morphs if morph.pos == '助詞']
                                if len(case) > 0:  # 助詞を含むchunkの場合は助詞と項を取得
                                    cases = cases + case
                                    modi_chunks.append(''.join(morph.surface for morph in sentence.chunks[src_r].morphs if morph.pos != '記号'))
                            if len(cases) > 0:  # 助詞が1つ以上見つかった場合は重複除去後辞書順にソートし、項と合わせて出力
                                cases = sorted(list(set(cases)))
                                tmp1=" ".join(cases)
                                tmp2=" ".join(modi_chunks)
                                line = f'{predicate}\t{tmp1}\t{tmp2}'
                                print(line, file=f)
                            break


# In[ ]:




