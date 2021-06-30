#!/usr/bin/env python
# coding: utf-8

# In[10]:


#cat q45.txt | sort | uniq -c | sort -nr | head -n 10
#cat q45.txt | grep "行う" | sort | uniq -c | sort -nr | head -n 3
#cat q45.txt | grep "なる" | sort | uniq -c | sort -nr | head -n 3
#cat q45.txt | grep "与える" | sort | uniq -c | sort -nr | head -n 3
from q41 import parse_q41
sentences=parse_q41()

#形態素を順番に見ていき、動詞であればかかり元文節を呼び出す
#かかり元文節中に助詞があれば、それらをリストに追加
#リストをタブ区切りでファイルに出力

with open("q45.txt", "w") as f:
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
                    
                    #かかり元となる文節について
                    for src_idxs in chunk.srcs:
                        
                        #各形態素について
                        for  morpheme_src in sentence.chunks[src_idxs].morphs:                 
                            #助詞であれば
                            if(morpheme_src.pos=="助詞"):
                                #リストに追加
                                cases=cases+[morpheme_src.surface]
                    #助詞のリストが空でなければ
                    if len(cases) > 0:
                        #一旦集合に入れて重複を除去し、その後リストに直してソートする
                        cases = sorted(list(set(cases)))
                        cases_str=" ".join(cases)
                        line = f"{morpheme.base}\t{cases_str}"
                        print(line, file=f)
                        
                    break


# In[ ]:




