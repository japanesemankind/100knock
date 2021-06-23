#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import transformers
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertModel
from torch import optim
from torch import cuda
import time
from matplotlib import pyplot as plt
from q86 import read_csv
import pandas as pd
from sklearn.model_selection import train_test_split

# Datasetの定義
class CreateDataset(Dataset):
    def __init__(self, X, y, tokenizer, max_len):
        self.X = X
        self.y = y
        self.tokenizer = tokenizer
        self.max_len = max_len
        
    def __len__(self):  # len(Dataset)で返す値を指定
        
        return len(self.y)
    
    def __getitem__(self, index):  # Dataset[index]で返す値を指定
        text = self.X[index]
        inputs = self.tokenizer.encode_plus(#BERTのtokenizerに渡す
            text,
            add_special_tokens=True,#トークン列の開始と終了を表す特殊トークンを挿入
            max_length=self.max_len,
            pad_to_max_length=True#max_lenにパディング
        )
        
        ids = inputs["input_ids"]
        mask = inputs["attention_mask"]
        
        return {
            "ids": torch.LongTensor(ids),
            "mask": torch.LongTensor(mask),
            "labels": torch.Tensor(self.y[index])
        }
    
# BERT分類モデルの定義
class BERTClass(torch.nn.Module):
    def __init__(self, drop_rate, otuput_size):
        super().__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.drop = torch.nn.Dropout(drop_rate)
        self.fc = torch.nn.Linear(768, otuput_size)  # BERTの出力に合わせて768次元を指定
        
    def forward(self, ids, mask):
        _, out = self.bert(ids, attention_mask=mask,return_dict=False)
        out = self.fc(self.drop(out))
        
        return out

def calculate_loss_and_accuracy(model, criterion, loader, device):
    """ 損失・正解率を計算"""
    model.eval()
    loss = 0.0
    total = 0
    correct = 0
    
    with torch.no_grad():
        for data in loader:
            # デバイスの指定
            ids = data["ids"].to(device)
            mask = data["mask"].to(device)
            labels = data["labels"].to(device)
            
        outputs = model(ids, mask)# 順伝播
        loss += criterion(outputs, labels).item()# 損失計算
        
        # 正解率計算
        pred = torch.argmax(outputs, dim=-1).cpu().numpy() # バッチサイズの長さの予測ラベル配列
        labels = torch.argmax(labels, dim=-1).cpu().numpy()  # バッチサイズの長さの正解ラベル配列
        total += len(labels)
        correct += (pred == labels).sum().item()
        
        return loss / len(loader), correct / total


def train_model(dataset_train, dataset_valid, batch_size, model, criterion, optimizer, num_epochs, device=None):
    """モデルの学習を実行し、損失・正解率のログを返す"""
    
    model.to(device)# デバイスの指定
    
    # dataloaderの作成
    dataloader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
    dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
    
    # 学習
    log_train = []
    log_valid = []
    
    for epoch in range(num_epochs):
        # 開始時刻の記録
        s_time = time.time()
        
        # 訓練モードに設定
        model.train()
        
        
        for data in dataloader_train:
            # デバイスの指定
            ids = data["ids"].to(device)
            mask = data["mask"].to(device)
            labels = data["labels"].to(device)
            optimizer.zero_grad()# 勾配をゼロで初期化
            
            # 順伝播 + 誤差逆伝播 + 重み更新
            outputs = model(ids, mask)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
        # 損失と正解率の算出
        loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train, device)
        loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid, device)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])
        
        # 終了時刻の記録
        e_time = time.time()
        
        # ログを出力
        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, accuracy_train: {acc_train:.4f}, loss_valid: {loss_valid:.4f}, accuracy_valid: {acc_valid:.4f}, {(e_time - s_time):.4f}sec') 
        
    return {'train': log_train, 'valid': log_valid}

def dfs_freeze(model):#モデルの全重みを凍結する
    for name, child in model.named_children():
        for param in child.parameters():
            param.requires_grad = False
        dfs_freeze(child)

if __name__=="__main__":
    
    # データの読込
    df = pd.read_csv('./newsCorpora.csv', header=None, sep='\t', names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
    
    # データの抽出
    df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['TITLE', 'CATEGORY']]
    
    # データの分割
    train, valid_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=123, stratify=df['CATEGORY'])
    valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=123, stratify=valid_test['CATEGORY'])
    
    train.reset_index(drop=True, inplace=True)
    valid.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)
    
    y_train = pd.get_dummies(train, columns=['CATEGORY'])[['CATEGORY_b', 'CATEGORY_e', 'CATEGORY_t', 'CATEGORY_m']].values
    y_valid = pd.get_dummies(valid, columns=['CATEGORY'])[['CATEGORY_b', 'CATEGORY_e', 'CATEGORY_t', 'CATEGORY_m']].values
    y_test = pd.get_dummies(test, columns=['CATEGORY'])[['CATEGORY_b', 'CATEGORY_e', 'CATEGORY_t', 'CATEGORY_m']].values
    
    # Datasetの作成
    max_len = 20
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    dataset_train = CreateDataset(train['TITLE'], y_train, tokenizer, max_len)
    dataset_valid = CreateDataset(valid['TITLE'], y_valid, tokenizer, max_len)
    dataset_test = CreateDataset(test['TITLE'], y_test, tokenizer, max_len)
    
    # パラメータの設定
    DROP_RATE = 0.4
    OUTPUT_SIZE = 4
    BATCH_SIZE = 32
    NUM_EPOCHS = 4
    LEARNING_RATE = 2e-5
    
    model = BERTClass(DROP_RATE, OUTPUT_SIZE)# モデルの定義
    
    #fc層以外の重みを凍結
    dfs_freeze(model)
    model.fc.requires_grad_(True)


    criterion = torch.nn.BCEWithLogitsLoss()# 損失関数の定義
    optimizer = torch.optim.AdamW(params=model.parameters(), lr=LEARNING_RATE)# オプティマイザの定義
    device = "cuda" if cuda.is_available() else "cpu"# デバイスの指定
    log = train_model(dataset_train, dataset_valid, BATCH_SIZE, model, criterion, optimizer, NUM_EPOCHS, device=device)# モデルの学習


# In[ ]:




