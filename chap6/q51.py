#!/usr/bin/env python
# coding: utf-8

# In[1]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
#カンマ区切りはread_csv()、タブ区切りはread_tabel()を使用
df = pd.read_table("newsCorpora.csv",
                                   header=None,
                                   names=("ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIME"),
                                   sep="\t",
                                   encoding="UTF-8")
instance=df.query("PUBLISHER in ['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail']")
instance_loc=instance.loc[:,["CATEGORY","TITLE"]]
category_list=instance_loc.CATEGORY.values.tolist()
title_list=instance_loc.TITLE.values.tolist()


for i,title in enumerate(title_list):
    title=title.lower()
    title=re.sub('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]',"",title)#記号類を削除
    title=re.sub(" [0-9]+"," 0",title)#数字を0に置き換え
    title=re.sub(" [0-9]+(.+?) "," \\1 ",title)#3-appleのような表現をappleに置き換え
    title=re.sub("million|thouzand|billion|trillion|quadrillion","0",title)#位を示す数詞を0に置き換え
    title_list[i]=title
        #word=re.sub("[0-9]+","0",word)
#print(title_list)
#print(len(title_list))

#カテゴリ名を数値に変換
str_to_int={"b":0,"t":1,"e":2,"m":3}
for i,category in enumerate(category_list):
    category_list[i]=str_to_int[category]  
#print(category_list)

#データ量を軽くするため、出現頻度の低い単語を無視
vec_tfidf=TfidfVectorizer(min_df=0.01)
X=vec_tfidf.fit_transform(title_list)



print(type(X))
df=pd.DataFrame(X.toarray(), columns=vec_tfidf.get_feature_names())#pandas.df型に変換
df["CATEGORY"]=category_list#カテゴリ名を末尾に追加
train,valid=train_test_split(df,test_size=0.20)#訓練データと検証データに分割
valid,test=train_test_split(valid,test_size=0.25)#検証データを、検証データと評価データに再分割


#ファイル出力
train.to_csv("train.feature.txt", sep="\t",header=False,index=False)
valid.to_csv("valid.feature.txt", sep="\t",header=False,index=False)
test.to_csv("test,feature.txt", sep="\t",header=False,index=False)

#print(valid)
#print(df.query("PUBLISHER in ['Reuters','Huffington Post','Businessweek','Contactmusic.com','Daily Mail']"))
#ID タイトル URL 情報元 カテゴリ  ストーリー URLホスト名 日付


# In[ ]:




