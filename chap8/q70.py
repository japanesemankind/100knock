#!/usr/bin/env python
# coding: utf-8

# In[37]:


from gensim.models import KeyedVectors
import pandas as pd
import re
import torch
#from tqdm.notebook import trange
def load_data(filename):
    df=pd.read_table(filename,
                                   sep="\t",
                                   encoding="UTF-8")
    return df

def title_to_vec(title):
    words=[word for word in title.split() if word in model]#モデル内に存在する国名だけ、リストに追加
    word_vec=[model[word] for word in words]#リストから単語ベクトルを取り出す
    return torch.tensor(sum(word_vec) / len(word_vec))

if __name__=="__main__":
    model=KeyedVectors.load('q60_model.pt', mmap='r')
    df_train=load_data("train2.txt")
    df_valid=load_data("valid2.txt")
    df_test=load_data("test2.txt")
    
    
    X_train = torch.stack([title_to_vec(text) for text in df_train['TITLE']])
    torch.save(X_train, 'X_train.pt')
    X_valid = torch.stack([title_to_vec(text) for text in df_valid['TITLE']])
    torch.save(X_valid, 'X_valid.pt')
    X_test = torch.stack([title_to_vec(text) for text in df_test['TITLE']])
    torch.save(X_test, 'X_test.pt')
    
    category_to_int={"b":0,"t":1,"e":2,"m":3}
    
#    Y_train=[category_to_int(category) for category in df_train["CATEGORY"]
#    print
    
    Y_train=torch.tensor([category_to_int[category] for category in df_train["CATEGORY"]])
    torch.save(Y_train, 'Y_train.pt')
    Y_valid=torch.tensor([category_to_int[category] for category in df_valid["CATEGORY"]])
    torch.save(Y_valid, 'Y_valid.pt')
    Y_test=torch.tensor([category_to_int[category] for category in df_test["CATEGORY"]])
    torch.save(Y_test, 'Y_test.pt')
#    title_list=df_test.TITLE.values.tolist()
#    for i,title in enumerate(title_list):
        
            
#            print(word)
#    df_test.to_csv("test2.txt", sep="\t",index=False)
    
#print(model['United_States'])


# In[ ]:




