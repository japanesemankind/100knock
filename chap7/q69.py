#!/usr/bin/env python
# coding: utf-8

# In[4]:


import bhtsne
import numpy as np
from q67 import country_load_q67
from matplotlib import pyplot as plt
country_names,word_vec=country_load_q67("my_country_list_100.csv")

#print(word_vec[0])
vec_2=np.array(word_vec).astype(np.float64)#64bit浮動小数点の形式に変換
#print()
#print(vec_2[0])

#embedded = bhtsne.tsne(vec_2, dimensions=2)

#ハイパーパラメータ:perplexity,n_iter,rand_seed
embedded = bhtsne.tsne(vec_2, dimensions=2,perplexity=10)
print(embedded)
#embedded = bhtsne.tsne(np.array(word_vec).astype(np.float64), dimensions=2, rand_seed=123)
plt.figure(figsize=(20, 20))
plt.scatter(np.array(embedded).T[0], np.array(embedded).T[1])
for (x, y), name in zip(embedded, country_names):
    plt.annotate(name, (x, y))
plt.show()


# In[ ]:




