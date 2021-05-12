#!/usr/bin/env python
# coding: utf-8

# In[3]:


def parse_mecab():
    
    filename = './neko.txt.mecab'
    sentences=[]
    morphemes=[]
    with open(filename, mode='r') as f:
        for line in f:  # 1行ずつ読込
            
            fields = line.split('\t')
            if len(fields) == 2 or ( fields[0] != "" and  fields[0] == "EOS\n"):  # 文頭以外の空白と改行文字はスキップ
            # if not len(fields) == 2 or ( fields[0] != "" and  fields[0] == "EOS\n"):
            #    continue
                
                if line != 'EOS\n':  # 文末以外であれば
            # if line == 'EOS\n':
            #    continue
                    attr =  fields[1].split(',')#形態素解析はカンマ区切り
                    
                    if(attr[6]!="*\n"):#改行記号を無視
                        
                        morpheme= {'surface': fields[0], 'base': attr[6], 'pos': attr[0], 'pos1': attr[1]}#形態素を辞書型に格納
                        morphemes.append(morpheme)#辞書を単語リストに追加
                    
                else:  # 文末：形態素リストを文リストに追加
                    if(morphemes!=[]):
                        sentences.append(morphemes)
                        morphemes = []
    return sentences