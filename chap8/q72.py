#!/usr/bin/env python
# coding: utf-8

# In[1]:


from torch import nn
import torch
from q71 import SLPNet    
model = SLPNet(300, 4)  # 単層ニューラルネットワークの初期化
X_train=torch.load("X_train.pt")
Y_train=torch.load("Y_train.pt")

criterion = nn.CrossEntropyLoss()
l_1 = criterion(model(X_train[:1]), Y_train[:1])
model.zero_grad()  # 勾配をゼロで初期化
l_1.backward()  # 勾配を計算
print(f'損失: {l_1:.4f}')
print(f'勾配:\n{model.fc.weight.grad}')#300行4列の行列(y1に対する勾配,y2に対する勾配,y3に対する勾配,y4に対する勾配)

l = criterion(model(X_train[:4]), Y_train[:4])
model.zero_grad()
l.backward()
print(f'損失: {l:.4f}')
print(f'勾配:\n{model.fc.weight.grad}')


# In[ ]:




