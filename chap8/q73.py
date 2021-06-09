#!/usr/bin/env python
# coding: utf-8

# In[1]:


from torch.utils.data import Dataset
from torch import nn
import torch
from torch.utils.data import DataLoader
from q71 import SLPNet
class NewsDataset(Dataset):
    def __init__(self, X, y):  # datasetの構成要素を指定
        self.X = X
        self.y = y
        
    def __len__(self):  # len(dataset)で返す値を指定
        return len(self.y)

    def __getitem__(self, idx):  # dataset[idx]で返す値を指定
        return [self.X[idx], self.y[idx]]
    
if __name__=="__main__":
    X_train=torch.load("X_train.pt")
    Y_train=torch.load("Y_train.pt")
    X_valid=torch.load("X_valid.pt")
    Y_valid=torch.load("Y_valid.pt")
    X_test=torch.load("X_test.pt")
    Y_test=torch.load("Y_test.pt")
    
    # Datasetの作成
    dataset_train = NewsDataset(X_train, Y_train)
    dataset_valid = NewsDataset(X_valid, Y_valid)
    dataset_test = NewsDataset(X_test, Y_test)
    
    # Dataloaderの作成
    dataloader_train = DataLoader(dataset_train, batch_size=1, shuffle=True)
    dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
    dataloader_test = DataLoader(dataset_test, batch_size=len(dataset_test), shuffle=False)
    
    # モデルの定義
    model = SLPNet(300, 4)
    
    # 損失関数の定義
    criterion = nn.CrossEntropyLoss()
    
    # オプティマイザの定義
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)
    
    # 学習
    num_epochs = 10
    for epoch in range(num_epochs):
        # 訓練モードに設定
        model.train()
        loss_train = 0.0
        
        for i, (inputs, labels) in enumerate(dataloader_train):
            # 勾配をゼロで初期化
            optimizer.zero_grad()
            # 順伝播 + 誤差逆伝播 + 重み更新
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)#損失関数の計算
            loss.backward()
            optimizer.step()#重みの更新
            
            # 損失を記録
            loss_train += loss.item()
            
        # バッチ単位の平均損失計算
        loss_train = loss_train / i
    # 検証データの損失計算
    model.eval() 
    with torch.no_grad():
        inputs, labels = next(iter(dataloader_valid))
        outputs = model(inputs)
        loss_valid = criterion(outputs, labels)
    # ログを出力
    torch.save(model.to('cpu').state_dict(), 'model.pth')
    print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, loss_valid: {loss_valid:.4f}') 
    
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




