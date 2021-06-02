#!/usr/bin/env python
# coding: utf-8

# In[6]:


from gensim.models import KeyedVectors

#オプションmmapで、ディスクからの読み込みを高速化?
#公式ドキュメント:https://radimrehurek.com/gensim/models/keyedvectors.html
model=KeyedVectors.load('q60_model.pt', mmap='r')
i=0
with open("questions-words.txt", "r") as file_r,open("q64_out.txt","a") as file_w:
    for line in file_r:
        line_split=line.split()
        if(line[0]==":"):
            file_w.write(line)
        else:
            word_similarity=model.most_similar(positive=[line_split[1], line_split[2]], negative=[line_split[0]], topn=1)[0]
            #print(line.rstrip(" \n")+*word_similarity+"\n")
            #print(line.rstrip(" \n"))
            #print(*word_similarity)
            add=word_similarity[0]+" "+str(word_similarity[1])
            file_w.write(" ".join([line.rstrip(" \n"),word_similarity[0],str(word_similarity[1]),"\n"]))
            file_w.flush()
        print(str(i)+":"+line)
        i+=1


# In[ ]:




