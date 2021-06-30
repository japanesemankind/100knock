#!/usr/bin/env python
# coding: utf-8

# In[15]:


import re
import requests
from q25 import templates_extraction
def get_file():
    dic=templates_extraction()
    file_name=dic["国旗画像"].replace(" ","_")
    
    #mediawikiのAPIを使用
    #action:操作
    #title:ファイル名
    #prop:取得する構成要素
    #iiprop:どのファイル情報を取得するか
    #format:出力フォーマット
    url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': 'File: ' + file_name,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    result = requests.get(url,params=params)
    
    #取得したjsonファイルをテキスト形式に変換し、url部分を取得
    return re.search(r'"url":"(.+?)"', result.text).group(1)

if __name__=="__main__":
    print(get_file())

