#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Morph:
    
  def __init__(self, morph):
    surface, attr = morph.split('\t')
    attr = attr.split(',')
    self.surface = surface#表層形
    self.base = attr[6]#基本形
    self.pos = attr[0]#品詞
    self.pos1 = attr[1]#品詞細分類1
    
filename = "ai.ja.txt.parsed"

sentences = []
morphemes = []
with open(filename, mode='r') as f:
    for line in f:
        
        if line[0] == "*":  # 係り受け関係を表す行：スキップ
            continue
        elif line != "EOS\n": #文末以外なら
            
            morphemes.append(Morph(line))
            
        else:  # 文末であれば
            
            sentences.append(morphemes)
            
            morphemes = []

if __name__=="__main__":
    # 確認
    for m in sentences[2]:
        #vars:インスタンス情報を取得
        print(vars(m))


# In[ ]:




