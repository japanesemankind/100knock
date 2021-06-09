#!/usr/bin/env python
# coding: utf-8

# In[1]:


from torch.utils.data import Dataset
from torch import nn
import torch
from torch.utils.data import DataLoader
from q71 import SLPNet
from q73 import NewsDataset
from q74 import load_Dataloader
from matplotlib import pyplot as plt
import numpy as np
    
def calculate_loss_and_accuracy(model, criterion, loader):
    model.eval()#モデルを性能評価モードに設定
    
    #計算結果の初期化
    loss = 0.0
    total = 0
    correct = 0
    
    with torch.no_grad():#一旦、勾配計算用パラメータの保存を停止して
        for inputs, labels in loader:#データローダから入力とラベルのリストを取り出して
            
            outputs = model(inputs)#出力を受け取る
            loss += criterion(outputs, labels).item()#出力とラベルから損失関数を計算する
            pred = torch.argmax(outputs, dim=-1)#ラベルを予測
            total += len(inputs)#入力の事例数を求める
            correct += (pred == labels).sum().item()#正しく予測できた事例の数を求める
            
    return loss / len(loader), correct / total    

if __name__=="__main__":
    
    dataloader_train = load_Dataloader("train",1)
    dataloader_valid = load_Dataloader("valid",len(NewsDataset(torch.load("X_valid.pt"),torch.load("Y_valid.pt"))))
    dataloader_test = load_Dataloader("test",len(NewsDataset(torch.load("X_test.pt"),torch.load("Y_test.pt"))))
    
    # モデルの定義
    model = SLPNet(300, 4)
    
    # 損失関数の定義(交差エントロピー損失=-log(xiがyiに分類される確率))
    criterion = nn.CrossEntropyLoss()
    
    # オプティマイザ(重み更新に用いるアルゴリズム)の定義(学習率0.1のSGD(確率的勾配降下法))
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)
    
    num_epochs = 10#エポック数の設定
    
    #ログ保存用のリスト
    log_train = []
    log_valid = []

    for epoch in range(num_epochs):#各エポックで

        # 訓練モードに設定
        model.train()
#        loss_train = 0.0#lloss_trainの初期化
        
        for i, (inputs, labels) in enumerate(dataloader_train):
            # 勾配をゼロで初期化
            optimizer.zero_grad()
            # 順伝播 + 誤差逆伝播 + 重み更新
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)#損失関数の計算
            loss.backward()
            optimizer.step()#重みの更新
            
            
            #モデルの保存
#             torch.save({'epoch': epoch,
#                                  'model_state_dict': model.state_dict(),
#                                  'optimizer_state_dict': optimizer.state_dict()},
#                                  f'checkpoint{epoch + 1}.pt')
            
        #損失関数と正解率を計算
        loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train)
        loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])
                         
        #ログ出力
        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, loss_valid: {loss_valid:.4f}') 
#         fig, ax = plt.subplots(1, 2, figsize=(15, 5))
#         ax[0].plot(np.array(log_train).T[0], label='train')
#         ax[0].plot(np.array(log_valid).T[0], label='valid')
#         ax[0].set_xlabel('epoch')
#         ax[0].set_ylabel('loss')
#         ax[0].legend()
#         ax[1].plot(np.array(log_train).T[1], label='train')
#         ax[1].plot(np.array(log_valid).T[1], label='valid')
#         ax[1].set_xlabel('epoch')
#         ax[1].set_ylabel('accuracy')
#         ax[1].legend()
#         plt.show()
        
        
        
    # 検証データの損失計算
    model.eval() 
    with torch.no_grad():#勾配計算用パラメータの保存をやめて、
        inputs, labels = next(iter(dataloader_valid))#validationデータから、データを一つずつ取り出して
        outputs = model(inputs)#出力を受け取る
        loss_valid = criterion(outputs, labels)#損失関数を計算
        
    torch.save(model.to('cpu').state_dict(), 'model_q76.pth')#重みの保存
    
#出力
# epoch: 1, loss_train: 0.5478, loss_valid: 0.3877
# epoch: 2, loss_train: 0.3815, loss_valid: 0.3488
# epoch: 3, loss_train: 0.3503, loss_valid: 0.3288
# epoch: 4, loss_train: 0.3333, loss_valid: 0.3221
# epoch: 5, loss_train: 0.3226, loss_valid: 0.3201
# epoch: 6, loss_train: 0.3150, loss_valid: 0.3166
# epoch: 7, loss_train: 0.3093, loss_valid: 0.3169
# epoch: 8, loss_train: 0.3047, loss_valid: 0.3144
# epoch: 9, loss_train: 0.3007, loss_valid: 0.3150
# epoch: 10, loss_train: 0.2981, loss_valid: 0.3111


# In[ ]:




