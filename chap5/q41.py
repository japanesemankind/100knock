#!/usr/bin/env python
# coding: utf-8

# In[17]:


from q40 import Morph
class Chunk():
    def __init__(self, morphs, dst):
        self.morphs = morphs#形態素のリスト
        self.dst = dst#かかり先index
        self.srcs = []#かかり元index
class Sentence():
    def __init__(self, chunks):
        self.chunks = chunks
        #各インデックス、文節に対して
        for i, chunk in enumerate(self.chunks):
            
            #dstが不正な値でなければ
            if chunk.dst != -1:
                #dst個めの文節のsrcに、この文節のインデックスを追加
                self.chunks[chunk.dst].srcs.append(i)
                
def parse_q41():
    filename = './ai.ja.txt.parsed'
    sentences = []
    Chunks = []
    morphs = []
    with open(filename, mode='r') as f:
        for line in f:
            if line[0] == '*':  # 係り受け関係を表す行であれば
                if len(morphs) > 0:
                    #リストに文節を追加
                    Chunks.append(Chunk(morphs, dst))
                    morphs = []
                    #かかり先インデックスを取得
                dst = int(line.split(' ')[2].rstrip('D'))
            
            elif line != 'EOS\n':  # 文末以外であれば
                #リストに形態素を追加
                morphs.append(Morph(line))
            else:  # 文末であれば
                #リストに文節を追加(例外処理)
                Chunks.append(Chunk(morphs, dst))       
                #リストに文を追加
                sentences.append(Sentence(Chunks))
                #リストを初期化
                morphs = []
                Chunks = []
                #かかり先インデックスの初期化(例外処理用に-1)
                dst = -1
    return sentences
if __name__=="__main__":
    sentences=parse_q41()
    for chunk in sentences[5].chunks:
        print([morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs)


# In[ ]:




