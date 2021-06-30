#!/usr/bin/env python
# coding: utf-8

# In[26]:


#参考サイト
#https://qiita.com/ground0state/items/155b77f4c07e1a509a14
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
#カンマ区切りはread_csv()、タブ区切りはread_tabel()を使用
def load_data(filename):
    df=pd.read_table(filename,
                                   sep="\t",
                                   encoding="UTF-8")
    return df

if __name__=="__main__":
    df_train=load_data("train.txt")
    df_valid=load_data("valid.txt")
    df_test=load_data("test.txt")
    
    df = pd.concat([df_train, df_valid, df_test], axis=0)
    df.reset_index(drop=True, inplace=True)
    title_list=df.TITLE.values.tolist()
    for i,title in enumerate(title_list):
        title=title.lower()
        title=re.sub('[^\w\s]',"",title)#記号類を削除
        title=re.sub(" [0-9]+"," 0",title)#数字を0に置き換え
        title=re.sub(" [0-9]+(.+?) "," \\1 ",title)#3-appleのような表現をappleに置き換え
        title=re.sub("million|thouzand|billion|trillion|quadrillion","0",title)#位を示す数詞を0に置き換え
        title_list[i]=title
    df["TITLE"]=title_list#
    
    #訓練・開発データと、検証データに分割
    train_and_valid=df[:len(df_train)+len(df_valid)]
    test = df[len(df_train) + len(df_valid):]
    
    vec_tfidf = TfidfVectorizer(min_df=0.001)
    
    #tf-idfでベクトル化
    X_train_valid = vec_tfidf.fit_transform(train_and_valid['TITLE'])  # trainとvalidのみを用いる
    X_test = vec_tfidf.transform(test['TITLE'])#testもベクトル化
    
    #pd.dfに出力
    X_train_valid = pd.DataFrame(X_train_valid.toarray(), columns=vec_tfidf.get_feature_names())
    X_test = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names())
    
    # 訓練データ開発データに分割
    X_train = X_train_valid[:len(df_train)]
    X_valid = X_train_valid[len(df_train):]
    
    # データの保存
    X_train.to_csv("train.feature.txt", sep='\t', index=False)
    X_valid.to_csv("valid.feature.txt", sep='\t', index=False)
    X_test.to_csv("test.feature.txt", sep='\t', index=False)


# In[ ]:




