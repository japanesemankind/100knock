#!/usr/bin/env python
# coding: utf-8

# In[3]:


from torch.utils.data import Dataset
from torch import nn
import torch
from torch.utils.data import DataLoader
from q71 import SLPNet
from q73 import NewsDataset
from q74 import load_Dataloader
import time

def calculate_loss_and_accuracy(model, criterion, loader):
    model.eval()
    loss = 0.0
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model(inputs)
            loss += criterion(outputs, labels).item()
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels).sum().item()
            
    return loss / len(loader), correct / total


def train_model(dataloader_train, dataloader_valid,model, criterion, optimizer, num_epochs):
    
    # 学習
    log_train = []
    log_valid = []
    for epoch in range(num_epochs):
        # 開始時刻の記録
        s_time = time.time()
        
        # 訓練モードに設定 
        model.train()
        
        for inputs, labels in dataloader_train:
            # 勾配をゼロで初期化
            optimizer.zero_grad()
            # 順伝播 + 誤差逆伝播 + 重み更新
            outputs = model.forward(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
        # 損失と正解率の算出
        loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train)
        loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])
            
        # チェックポイントの保存
        torch.save({'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}, f'checkpoint{epoch + 1}.pt')
            
        # 終了時刻の記録
        e_time = time.time()
        
        # ログを出力
        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, accuracy_train: {acc_train:.4f}, loss_valid: {loss_valid:.4f}, accuracy_valid: {acc_valid:.4f}, {(e_time - s_time):.4f}sec') 
        
    return {'train': log_train, 'valid': log_valid}

if __name__=="__main__":

    
    model = SLPNet(300, 4)# モデルの定義    
    criterion = nn.CrossEntropyLoss()# 損失関数の定義
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)# オプティマイザの定義
    
    # モデルの学習
    for batch_size in [2 ** i for i in range(11)]:
        print(f'バッチサイズ: {batch_size}')
        dataloader_train = load_Dataloader("train",batch_size)
        dataloader_valid = load_Dataloader("valid", batch_size)
        
        log = train_model(dataloader_train, dataloader_valid,model, criterion, optimizer, 1)


# In[ ]:




