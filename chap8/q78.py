#!/usr/bin/env python
# coding: utf-8

# In[1]:


from q71 import SLPNet
from q74 import load_Dataloader
from torch import nn
import torch
import time

def calculate_loss_and_accuracy(model, criterion, loader, device):
    model.eval()
    loss = 0.0
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            loss += criterion(outputs, labels).item()
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels).sum().item()
            
    return loss / len(loader), correct / total


def train_model(dataloader_train, dataloader_valid, batch_size, model, criterion, optimizer, num_epochs, device=None):
    # GPUに送る
    model.to(device)
    
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
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model.forward(inputs)#出力を求める
            loss = criterion(outputs, labels)#損失関数の計算
            loss.backward()#誤差を求める
            optimizer.step()#重みの更新

    # 損失と正解率の算出
    loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train, device)
    loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid, device)
    log_train.append([loss_train, acc_train])
    log_valid.append([loss_valid, acc_valid])

    # チェックポイントの保存
    #torch.save({'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}, f'checkpoint{epoch + 1}.pt')

    # 終了時刻の記録
    e_time = time.time()

    # ログを出力
    print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, accuracy_train: {acc_train:.4f}, loss_valid: {loss_valid:.4f}, accuracy_valid: {acc_valid:.4f}, {(e_time - s_time):.4f}sec') 

    return {'train': log_train, 'valid': log_valid}
if __name__=="__main__":
    # datasetの作成
    dataloader_train = load_Dataloader("train",64)
    dataloader_valid = load_Dataloader("valid", 64)
    
    # モデルの定義
    model = SLPNet(300, 4)

    # 損失関数の定義
    criterion = nn.CrossEntropyLoss()
    
    # オプティマイザの定義
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)
    
    # デバイスの指定
    device = torch.device('cuda')
    
    # モデルの学習
    for batch_size in [2 ** i for i in range(11)]:
        print(f'バッチサイズ: {batch_size}')
        log = train_model(dataloader_train, dataloader_valid, batch_size, model, criterion, optimizer, 1, device=device)


# In[ ]:




