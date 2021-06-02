#!/usr/bin/env python
# coding: utf-8

# In[5]:


from gensim.models import KeyedVectors
#model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)
#model.save("q60_model.pt")
model=KeyedVectors.load('q60_model.pt', mmap='r')

print(model['United_States'])


# In[ ]:




