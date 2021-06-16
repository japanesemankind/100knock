#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
from torch import nn
from torch.utils.data import Dataset
import pandas as pd
from pytorch_model_summary import summary
import pickle

class my_RNN(nn.Module):
    def __init__(self,hidden_size, output_size,vocab_size,padding_idx):
        super().__init__()
        self.hidden_size = hidden_size
        self.emb = nn.Embedding(vocab_size,300,padding_idx=padding_idx)#例の通り、単語埋め込みの次元を300に設定
        self.rnn = nn.RNN(300,hidden_size,nonlinearity='tanh',batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        self.batch_size = x.size()[0]
        hidden=self.initHidden()  # h0のゼロベクトルを作成
        emb = self.emb(x)
        # emb.size() = (batch_size, seq_len, emb_size)
        out,hidden= self.rnn(emb, hidden)
        # out.size() = (batch_size, seq_len, hidden_size)
        out=self.fc(out[:, -1, :])#最後の単語の部分だけを取り出して、fc層に入力する。
        out=self.softmax(out)
        # out.size() = (batch_size, output_size)
        return out

    def initHidden(self):
        return torch.zeros(1,self.batch_size,self.hidden_size)

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
    #print(f"VOCAB_SIZE:{VOCAB_SIZE}")
    EMB_SIZE=300
    
    
    #パディングのサイズ=最長の系列長を求める
    df = pd.read_table("q80_converted_news.csv",
                       sep="\t",
                       encoding="UTF-8")
    PADDING_IDX=0
    for IDs in df.TITLE.values.tolist():
        
        #パディングサイズを更新
        if(len(IDs.split())>PADDING_IDX):
            PADDING_IDX=len(IDs.split())
            
    #print(f"PADDING_IDX:{PADDING_IDX}")
    
    
    # PADDING_IDX=len(word_ID)
    # print(f"PADDING_IDX:{PADDING_IDX}")
    OUTPUT_SIZE = 4
    HIDDEN_SIZE = 50#例の通り、隠れ層の次元を50*50に設定
    
    # モデルの定義
    my_model=my_RNN(HIDDEN_SIZE,OUTPUT_SIZE,VOCAB_SIZE,PADDING_IDX)
    
    X = Dataset_train[1][0]
    print(Dataset_train[0][0][0])
    X2=X.unsqueeze(0)
    #print(X)
    #print(X2)
    #print(summary(model,X2))
    print(summary(my_model,X2))
    print(my_model(X2))
    # print(my_model(X2))
    # print(my_model.state_dict())
    # emb_weight=my_model.state_dict()["emb.weight"]
    
    # rnn_ih_l0_weight=my_model.state_dict()["rnn.weight_ih_l0"]
    # rnn_hh_l0_weight=my_model.state_dict()["rnn.weight_hh_l0"]
    # rnn_bias_ih_l0=my_model.state_dict()["rnn.bias_ih_l0"]
    
    # fc_weight=my_model.state_dict()["fc.weight"]
    # fc_bias=my_model.state_dict()["fc.bias"]
    
    # print(f"バッチサイズ:{my_model.batch_size}")
    # print(f"emb_weight:{emb_weight.size()}")
    
    # print(f"rnn_ih_l0:{rnn_ih_l0_weight.size()}")
    # print(f"rnn_hh_l0:{rnn_hh_l0_weight.size()}")
    # print(f"rnn_bias_ih_l0:{rnn_bias_ih_l0.size()}")
    
    # print(f"fc_weight:{fc_weight.size()}")
    # print(f"fc_bias:{fc_bias.size()}")
    
    
    #print(len(emb_weight[0]))
    #print(torch.softmax(model(X2), dim=-1))


# In[ ]:





# In[ ]:




