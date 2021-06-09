#!/usr/bin/env python
# coding: utf-8

# In[6]:


from torch.utils.data import Dataset
from torch import nn
import torch
from torch.utils.data import DataLoader
from torchvision import models
from q71 import SLPNet

class NewsDataset(Dataset):
    def __init__(self, X, y):  # datasetの構成要素を指定
        self.X = X
        self.y = y
        
    def __len__(self):  # len(dataset)で返す値を指定
        return len(self.y)

    def __getitem__(self, idx):  # dataset[idx]で返す値を指定
        return [self.X[idx], self.y[idx]]
    
def calculate_accuracy(model, loader):
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model(inputs)
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels).sum().item()
            
    return correct / total    

def load_Dataloader(data_type,size):
    X=torch.load("X_"+data_type+".pt")
    Y=torch.load("Y_"+data_type+".pt")
    dataset=NewsDataset(X,Y)
    dataloader=DataLoader(dataset, batch_size=size, shuffle=True)
    return dataloader
    
    
if __name__=="__main__":
    
    dataloader_train = load_Dataloader("train",1)
    dataloader_valid = load_Dataloader("valid",len(NewsDataset(torch.load("X_valid.pt"),torch.load("Y_valid.pt"))))
    dataloader_test = load_Dataloader("test",len(NewsDataset(torch.load("X_test.pt"),torch.load("Y_test.pt"))))
    
    # モデルの定義
    model = SLPNet(300, 4)
    model.load_state_dict(torch.load('model.pth'))
    
    acc_train = calculate_accuracy(model, dataloader_train)
    acc_test = calculate_accuracy(model, dataloader_test)
    print(f'正解率（学習データ）：{acc_train:.3f}')
    print(f'正解率（評価データ）：{acc_test:.3f}')


# In[ ]:




