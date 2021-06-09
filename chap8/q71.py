#!/usr/bin/env python
# coding: utf-8

# In[1]:


from torch import nn
import torch
class SLPNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        nn.init.normal_(self.fc.weight, 0.0, 1.0)  # 正規乱数で重みを初期化
        
    def forward(self, x):
        x = self.fc(x)
        return x
    
if __name__=="__main__":
    model = SLPNet(300, 4)  # 単層ニューラルネットワークの初期化
    X_train=torch.load("X_train.pt")
    
    #print(X_train[0])
    
    input1=X_train[0]
    input2=X_train[:4]
    print(input1)
    print(input2)
    
    #print(model.state_dict())#ネットワークの重みを表示(4行300列の行列)
    #print(model.fc.weight)
    
    y_hat_1 = torch.softmax(model(input1), dim=-1)
    print(y_hat_1)#4次元のベクトル
    
    Y_hat = torch.softmax(model.forward(input2), dim=-1)
    print(Y_hat)#4次元のベクトル


# In[ ]:




