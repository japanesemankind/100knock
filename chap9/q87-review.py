#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset
import pandas as pd
from pytorch_model_summary import summary
import pickle
#from q86 import my_CNN
from q86 import read_csv
from q86 import my_Dataset
from q85 import calculate_loss_and_accuracy
from q85 import padding_batch
from torch.utils.data import DataLoader

class my_CNN(torch.nn.Module):
    def __init__(self,dw,dh,n_vocab,padding_idx,max_len):
        super().__init__()
        #self.emb = torch.nn.Embedding(n_vocab,dw,padding_idx,max_len)
        self.emb = torch.nn.Embedding(n_vocab,dw)
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

def train_model(output_size,vocab_size,padding_idx):
    train=read_csv("train.csv")
    valid=read_csv("valid.csv")
    test=read_csv("test.csv")
    dataset_train=my_Dataset(train["TITLE"],train["CATEGORY"])
    dataset_valid=my_Dataset(valid["TITLE"],valid["CATEGORY"])
    dataset_test=my_Dataset(test["TITLE"],test["CATEGORY"])
    
    dataloader_train = DataLoader(dataset_train, batch_size=64, shuffle=True,collate_fn=padding_batch)
    dataloader_valid = DataLoader(dataset_valid, batch_size=64, shuffle=True,collate_fn=padding_batch)
    dataloader_test = DataLoader(dataset_test, batch_size=64, shuffle=True,collate_fn=padding_batch)
        
    device=torch.device('cuda')    
    
    my_model=my_CNN(300,50,vocab_size,padding_idx,10)#モデルの定義
    criterion = nn.CrossEntropyLoss()#損失関数の定義
    optimizer = torch.optim.SGD(my_model.parameters(), lr=1e-1)#オプティマイザの定義
    
    num_epochs=10
    log_train = []
    log_valid = []
    my_model.to(device)
    for epoch in range(num_epochs):
        # 訓練モードに設定
        my_model.train()
        loss_train = 0.0
        
        for data in dataloader_train:
            # 勾配をゼロで初期化
            optimizer.zero_grad()
            # 順伝播 + 誤差逆伝播 + 重み更新
            
            inputs=data[0].to(device)
            labels=data[1].to(device)
            
            outputs = my_model(inputs)
            
            loss = criterion(outputs, labels)#損失関数の計算
            loss.backward()
            optimizer.step()#重みの更新
            
        #損失関数と正解率を計算        
        loss_train, acc_train = calculate_loss_and_accuracy(my_model, criterion, dataloader_train,device)
        loss_valid, acc_valid = calculate_loss_and_accuracy(my_model, criterion, dataloader_valid,device)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])
                         
        #ログ出力
        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f} , acc_train: {acc_train:.4f} , loss_valid: {loss_valid:.4f} , acc_valid: {acc_valid:.4f}')
        
    #検証データの損失計算
    my_model.eval() 
    with torch.no_grad():
        inputs, labels = next(iter(dataloader_valid))
        inputs=inputs.to(device)
        labels=labels.to(device)
        outputs = my_model(inputs)
        loss_valid = criterion(outputs, labels)
        
    torch.save(my_model.to(device).state_dict(), 'q87_model.pth')#パラメータの保存
    return {"train": log_train, "valid": log_valid}



    
if __name__=="__main__":
    
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
    
    log=train_model(OUTPUT_SIZE,VOCAB_SIZE,PADDING_IDX)


# In[ ]:




