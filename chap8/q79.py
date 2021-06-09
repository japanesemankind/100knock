#!/usr/bin/env python
# coding: utf-8

# In[63]:


from torch.utils.data import Dataset
from torch import nn
import torch
from torch.utils.data import DataLoader
#from q71 import SLPNet
from q73 import NewsDataset
from q74 import load_Dataloader
import time
from torch.nn import functional as F

class SLPNet(nn.Module):
    def __init__(self, input_size, output_size,mid_size):        
        super().__init__()
        self.fc = nn.Linear(input_size,mid_size,bias=False)        
        self.fc2= nn.Linear(mid_size, mid_size)
        self.fc3=nn.Linear(mid_size, output_size)
        #正則化とドロップアウトを追加
        self.dropout = nn.Dropout(0.3)
        self.bn = nn.BatchNorm1d(mid_size)
        nn.init.normal_(self.fc.weight, 0.0, 1.0)  # 正規乱数で重みを初期化
        
    def forward(self, x):
        x = F.relu(self.fc(x))
        #x = F.relu(self.fc2(x))
        #x = self.dropout(x)
        x = F.relu(self.bn(x))
        x = self.dropout(x)
        x = F.relu(self.fc3(x))        
#        x = self.relu(x)
#        x = self.dropout(x)
        
        return x


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


def train_model(dataloader_train, dataloader_valid,model, criterion, optimizer, num_epochs, device=None):
    # GPUに送る
    model.to(device)

    
    # 学習
    log_train = []
    log_valid = []
    
    scheduler =torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, num_epochs, eta_min=1e-5, last_epoch=-1)
    #cosカーブに従って、学習率を変化させる
    #引数:オプティマイザ、半周期の長さ、最小学習率
    
    #scheduler = torch.optim.lr_scheduler.StepLR(optimizer,num_epochs/5,0.5)
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
            outputs = model.forward(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
        # 損失と正解率の算出
        loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train, device)
        loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid, device)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])
            
        # チェックポイントの保存
#        torch.save({'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}, f'checkpoint{epoch + 1}.pt')
            
        # 終了時刻の記録
        e_time = time.time()
        
        # ログを出力
        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, accuracy_train: {acc_train:.4f}, loss_valid: {loss_valid:.4f}, accuracy_valid: {acc_valid:.4f}, {(e_time - s_time):.4f}sec') 
        
#        if epoch > 2 and log_valid[epoch - 4][0] <= log_valid[epoch - 3][0] <= log_valid[epoch - 2][0] <= log_valid[epoch - 1][0] <= log_valid[epoch][0]:
#            break
        scheduler.step()
    return {'train': log_train, 'valid': log_valid}

if __name__=="__main__":

    
    model = SLPNet(300, 4,200)# モデルの定義    
    criterion = nn.CrossEntropyLoss()# 損失関数の定義
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)# オプティマイザの定義
    #optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
    device = torch.device('cuda')# デバイスの指定
    
    # モデルの学習
    dataloader_train = load_Dataloader("train",64)
    dataloader_valid = load_Dataloader("valid", 64)
    dataloader_test = load_Dataloader("test", 64)
    log = train_model(dataloader_train, dataloader_valid,model, criterion, optimizer, 100,device=device)
    
    loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train, device)
    loss_test, acc_test = calculate_loss_and_accuracy(model, criterion, dataloader_test, device)
    print(f"学習データでの正解率:{acc_train}")
    print(f"評価データでの正解率:{acc_test}")


# In[ ]:




