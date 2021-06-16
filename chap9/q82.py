#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
from torch import nn
from torch.utils.data import Dataset
import pandas as pd
from pytorch_model_summary import summary
import pickle
from torch.utils.data import DataLoader
from q81 import ID2List
from q81 import read_csv
class my_RNN(nn.Module):
    def __init__(self,hidden_size, output_size,vocab_size,padding_idx,device):
        super().__init__()
        self.device=device
        self.hidden_size = hidden_size
        self.emb = nn.Embedding(vocab_size,300,padding_idx=padding_idx)#例の通り、単語埋め込みの次元を300に設定
        self.rnn = nn.RNN(300,hidden_size,nonlinearity='tanh',batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        self.batch_size = x.size()[0]
        hidden=self.initHidden().to(self.device)  # h0のゼロベクトルを作成
        emb = self.emb(x)
        # emb.size() = (batch_size, seq_len, emb_size)
        out,hidden= self.rnn(emb, hidden)
        # out.size() = (batch_size, seq_len, hidden_size)
        out=self.fc(out[:, -1, :])#最後の単語の部分(xT)だけを取り出して、fc層に入力する。
        out=self.softmax(out)
        # out.size() = (batch_size, output_size)
        return out

    def initHidden(self):
        return torch.zeros(1,self.batch_size,self.hidden_size)
    

def calculate_loss_and_accuracy(model, criterion, loader,device):
    model.eval()
    model.to(device)
#    print(model.device)
    loss = 0.0
    total = 0
    correct = 0
    with torch.no_grad():
        for i,data in enumerate(loader):
            
            inputs=data[0].to(device)
            labels=data[1].to(device)
#             if(i==0):
#                 print(f"モデル:{model.device}")                
#                 print(f"入力:{inputs.device}")
#                 print(f"ラベル:{inputs.device}")
#             inputs.to(device)
#             labels.to(device)
            
            outputs = model(inputs)
            outputs.to(device)
#            print(outputs.get_device())
            loss += criterion(outputs, labels).item()
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels).sum().item()
            
    return loss / len(loader), correct / total     
    

class my_Dataset(Dataset):
    def __init__(self,X,Y):#初期化時に実行される関数
        self.X=X
        self.Y=Y
        
    def __len__(self):#len()関数で、返す値を決定する関数
        return len(self.Y)
    
    def __getitem__(self,idx):#インデックス指定で、返すものを決定する関数
        #return torch.tensor(self.X[idx],dtype=torch.int32),torch.tensor(self.Y[idx],dtype=torch.int32)
        return torch.tensor(self.X[idx]),torch.tensor(self.Y[idx])
    
def train_model(hidden_size,output_size,vocab_size,padding_idx):
    train=read_csv("train.csv")
    valid=read_csv("valid.csv")
    test=read_csv("test.csv")
    dataset_train=my_Dataset(train["TITLE"],train["CATEGORY"])
    dataset_valid=my_Dataset(valid["TITLE"],valid["CATEGORY"])
    dataset_test=my_Dataset(test["TITLE"],test["CATEGORY"])
    
    dataloader_train = DataLoader(dataset_train, batch_size=1, shuffle=False)
    dataloader_valid = DataLoader(dataset_valid, batch_size=1, shuffle=False)
    dataloader_test = DataLoader(dataset_test, batch_size=1, shuffle=False)
    
    # モデルの定義
    
    device=torch.device('cuda')
    
    my_model=my_RNN(hidden_size,output_size,vocab_size,padding_idx,device)
    criterion = nn.CrossEntropyLoss()#損失関数の定義
    optimizer = torch.optim.SGD(my_model.parameters(), lr=1e-1)#オプティマイザの定義
    
    num_epochs = 5
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
#            print(outputs)
#             print(f"{type(outputs)}:{outputs}")
#             print(f"{type(labels)}:{labels}")
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
        
    torch.save(my_model.to(device).state_dict(), 'q82_model.pth')#パラメータの保存
    return {"train": log_train, "valid": log_valid}


if __name__=="__main__":
    with open("q80_wordIDs.dict", mode='rb') as f:
        word_ID=pickle.load(f)
        
    VOCAB_SIZE=len(word_ID) + 1  # 辞書のID数 + パディングID
    
    df = pd.read_table("q80_converted_news.csv",sep="\t",encoding="UTF-8")
    PADDING_IDX=0    
    for IDs in df.TITLE.values.tolist():
        #パディングサイズを更新
        if(len(IDs.split())>PADDING_IDX):
            PADDING_IDX=len(IDs.split())
            
    log=train_model(50,4,VOCAB_SIZE,PADDING_IDX)


# In[ ]:




