#!/usr/bin/env python
# coding: utf-8

# In[1]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from q51_2 import load_data
lr=pickle.load(open("my_lr.model", 'rb'))

train_feature=load_data("train.feature.txt")
train=load_data("train.txt")
test_feature=load_data("test.feature.txt")
test=load_data("test.txt")
pred_train=lr.predict(train_feature)
pred_test=lr.predict(test_feature)
cm_train=confusion_matrix(train["CATEGORY"], pred_train)
cm_test=confusion_matrix(test["CATEGORY"], pred_test)
print(cm_test)
sns.heatmap(cm_train, square=True, cbar=True, annot=True, cmap='Blues')
plt.show()
plt.clf()
sns.heatmap(cm_test, square=True, cbar=True, annot=True, cmap='Blues')
plt.show()


# In[ ]:




