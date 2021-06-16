#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import re
from collections import defaultdict
import pickle

def title2ID(title):
    with open("q80_wordIDs.dict", mode='rb') as f:
        word_ID=pickle.load(f)
    converted_title=[]
        
    for word in title.split():
        if not (word in word_IDs):
            converted_title.append(0)
        else:
            converted_title.append(word_IDs[word])
        
    return converted_title       
    #return " ".join(map(str,converted_title))
        
if __name__=="__main__":
    df = pd.read_table("my_newsCorpora.csv",
                                   sep="\t",
                                   encoding="UTF-8")
    title_list=df.TITLE.values.tolist()
    with open("q80_wordIDs.dict", mode='rb') as f:
            word_IDs=pickle.load(f)
#     word_IDs=defaultdict(int)
    
#     word_counter=defaultdict(int)
#     for title in title_list:
        
#         for word in title.split():
#             word_counter[word]+=1
            
#     sorted_word_counter=sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    
#     ID=1
#     for pair in sorted_word_counter:
#         key=pair[0]
#         value=pair[1]
        
#         if(value<2):
#             break
#         word_IDs[key]=ID
#         ID+=1

#     #IDの辞書を保存
#     with open("q80_wordIDs.dict", mode='wb') as f:
#         pickle.dump(word_IDs,f)

    
    for i,title in enumerate(title_list):
        converted_title=[]
        
        for word in title.split():
            if not (word in word_IDs):
                converted_title.append(0)
            else:
                converted_title.append(word_IDs[word])
        #title_list[i]=converted_title        
        title_list[i]=" ".join(map(str,converted_title))
    df["TITLE"]=title_list
    df.to_csv("q80_converted_news.csv", sep='\t', index=False)
# sorted_word_counter=sorted(word_counter.items(), key=lambda x: x[1], reverse=True)

# word_IDs=defaultdict(int)

# ID=0
# for pair in sorted_word_counter:
#     key=pair[0]
#     value=pair[1]
    
#     if(value<2):
#         break
#     word_IDs[key]=ID
#     ID+=1
    
# #IDの辞書を保存
# with open("q80_wordIDs.dict", mode='wb') as f:
#     pickle.dump(word_IDs,f)


# In[ ]:




