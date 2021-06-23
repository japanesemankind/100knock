#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset
import pandas as pd
from pytorch_model_summary import summary
import pickle

class my_CNN(nn.Module):
    def __init__(self, output_size,vocab_size,padding_idx):
        super().__init__()
        self.emb = nn.Embedding(vocab_size,300,padding_idx=padding_idx)#例の通り、単語埋め込みの次元を300に設定
        self.conv = nn.Conv2d(1,100, (3, 300),1, (1, 0))
        self.fc = nn.Linear(100, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        # x.size() = (batch_size, seq_len)
        emb = self.emb(x).unsqueeze(1)
        # emb.size() = (batch_size, 1, seq_len, emb_size)
        conv = self.conv(emb)
        # conv.size() = (batch_size, out_channels, seq_len, 1)
        act = F.relu(conv.squeeze(3))
        # act.size() = (batch_size, out_channels, seq_len)
        max_pool = F.max_pool1d(act, act.size()[2])
        # max_pool.size() = (batch_size, out_channels, 1) -> seq_len方向に最大値を取得
        out = self.fc(max_pool.squeeze(2))
        out=self.softmax(out)
        # out.size() = (batch_size, output_size)
        return out
    
    
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
    my_model=my_CNN(OUTPUT_SIZE,VOCAB_SIZE,PADDING_IDX)
    
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




