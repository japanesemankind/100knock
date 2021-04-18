#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
def q9(str_arg):
    result=""
    words=str_arg.split()
    
    for word in words:
        result+=shuffle_word(word)
        result+=" "
        
    #最後に入る余分なスペースを無視
    return result[:-1]
def shuffle_word(word):
    shaffled=""
    if(len(word)>4):
        shaffled+=word[0]
        shaffled+="".join(random.sample(word[1:-1],len(word[1:-1])))
        shaffled+=word[-1]
        return shaffled
    else:
        return word
#print(shuffle_word("ABC"))

print(q9("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))


# In[ ]:




