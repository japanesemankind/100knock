#!/usr/bin/env python
# coding: utf-8

# In[22]:


#cat q46.txt | head -n 3
from q41 import parse_q41
sentences=parse_q41()

#形態素を順番に見ていき、動詞であればかかり元文節を呼び出す
#かかり元文節を中に助詞があれば、それらをリストに追加
#また、かかり元文節のリストを作成
#リストをタブ区切りでファイルに出力

with open("q46.txt", "w") as f:
    #文のリストを走査
    for sentence in sentences:
        #文節のリストを走査
        for chunk in sentence.chunks:
            #形態素のリストを走査
            for morpheme in chunk.morphs:
                
                #形態素が動詞であれば
                if morpheme.pos == "動詞":
                    #かかり元のリストを作成
                    cases = []
                    
                    chunk_srcs=[]
                    #かかり元となる文節について
                    for src_idx in chunk.srcs:
                        #各形態素について
                        tmp=[]
                        for  morpheme_src in sentence.chunks[src_idx].morphs:                 
                            #助詞であれば
                            if(morpheme_src.pos=="助詞"):
                                #リストに追加
                                cases=cases+[morpheme_src.surface]
                                
                            #文字列リストを連結
                            tmp+=morpheme_src.surface
#                            print(morpheme_src.surface)
#                        print(tmp)
                        #文字列に変換し、かかり元文節のリストに追加
                        chunk_srcs=chunk_srcs+["".join(tmp)]
#                        print(chunk_srcs)
                    #助詞のリストが空でなければ
                    if len(cases) > 0:
#                        print(chunk_srcs)
                        #一旦集合に入れて重複を除去し、その後リストに直してソートする
                        cases = sorted(list(set(cases)))
                        cases_str=" ".join(cases)
                        chunk_srcs=sorted(list(set(chunk_srcs)))
                        chunk_srcs_str=" ".join(chunk_srcs)
                        line = f"{morpheme.base}\t{cases_str}\t{chunk_srcs_str}"
                        print(line, file=f)
                        
                    break


# In[ ]:




