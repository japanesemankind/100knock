#!/usr/bin/env python
# coding: utf-8

# In[31]:


import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset
import pandas as pd
from pytorch_model_summary import summary
import pickle
from pytorch_model_summary import summary

#ネットワークレイヤーのパラメータをグローバル変数で指定


class my_CNN(torch.nn.Module):
    def __init__(self,dw,dh,n_vocab,padding_idx,max_len):
        super().__init__()
        self.emb = torch.nn.Embedding(n_vocab,dw,padding_idx,max_len)
        
        self.conv = torch.nn.Conv1d(dw,dh,3,padding=1)#時刻t-1,t,t+1のベクトルを連結した行列に対し、重み行列との積を取る。
        self.relu = torch.nn.ReLU()
        self.pool = torch.nn.MaxPool1d(max_len)#各時刻の特徴ベクトルの中から、最大のものを取り出す。
        self.linear = torch.nn.Linear(dh,4)
        self.softmax = torch.nn.Softmax(dim=1)
    def forward(self, x, h=None):
        x=self.emb(x)
        x=x.view(x.shape[0], x.shape[2], x.shape[1])
        x=self.conv(x)
        x=self.relu(x)
        x=x.view(x.shape[0], x.shape[1], x.shape[2])
        x=self.pool(x)
        x=x.view(x.shape[0], x.shape[1])
        y=self.linear(x)
        y=self.softmax(y)
        return y
    
    
def ID2List(title):
    title_list=[]
    for ID in title.split():
        title_list.append(int(ID))
    return title_list

def read_csv(filepath):
    category_to_label={"b":0,"t":1,"e":2,"m":3}
    df=pd.read_table(filepath,sep="\t",encoding="UTF-8")
    df["TITLE"]=[ID2List(title) for title in df["TITLE"]]
    df["CATEGORY"]=[category_to_label[category] for category in df["CATEGORY"]]
    return df

class my_Dataset(Dataset):
    def __init__(self,X,Y):#初期化時に実行される関数
        self.X=X
        self.Y=Y
        
    def __len__(self):#len()関数で、返す値を決定する関数
        return len(self.Y)
    
    def __getitem__(self,idx):#インデックス指定で、返すものを決定する関数
        return torch.tensor(self.X[idx]),torch.tensor(self.Y[idx])
        #return torch.tensor(self.X[idx],dtype=torch.int32),torch.tensor(self.Y[idx],dtype=torch.int32)
    
    
if __name__=="__main__":
    train=read_csv("train.csv")
    valid=read_csv("valid.csv")
    test=read_csv("test.csv")
    
    Dataset_train=my_Dataset(train["TITLE"],train["CATEGORY"])
    #Dataset_valid=my_Dataset(valid["TITLE"],valid["CATEGORY"])
    #Dataset_test=my_Dataset(test["TITLE"],test["CATEGORY"])
    
    #print(Dataset_train[0])
    #print(len(Dataset_train))
    
    # パラメータの設定
    with open("q80_wordIDs.dict", mode='rb') as f:
        word_ID=pickle.load(f)
    #print(len(word_ID))
    VOCAB_SIZE=len(word_ID) + 1  # 辞書のID数 + パディングID
    
    
    #パディングのサイズ=最長の系列長を求める
    df = pd.read_table("q80_converted_news.csv",
                       sep="\t",
                       encoding="UTF-8")
    PADDING_IDX=0
    for IDs in df.TITLE.values.tolist():
        
        #パディングサイズを更新
        if(len(IDs.split())>PADDING_IDX):
            PADDING_IDX=len(IDs.split())
    
    OUTPUT_SIZE = 4
    
    # モデルの定義
    my_model=my_CNN(300,50,VOCAB_SIZE,PADDING_IDX,10)
    X = Dataset_train[1][0]
    #X=torch.tensor([[250,684,0,1135,6,1599,1136,0],[42,0,38,0,40,640,1484,1]])
    X2=X.unsqueeze(0)
    
    print(f"出力:{my_model(X2)}")
    print(summary(my_model,X2))
    
    model_state=my_model.state_dict()
    for layer_name in model_state:
        layer_weight=my_model.state_dict()[layer_name]
        print(f"[{layer_name}]:{layer_weight.size()}")


# In[ ]:




