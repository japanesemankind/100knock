#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x_range=0
    score_list=[]
    with open("q94_bleu_log.txt") as f:
        for line in f:
            bleu_score=line.split(" ")[2]
            x_range+=1
            score_list.append(bleu_score)
    x_axis=[x for x in range(1,x_range+1)]
    plt.plot(x_axis, score_list)
    plt.show()


# In[ ]:




