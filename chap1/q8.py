#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cipher(str_arg):
    encrypted=""
    decrypted=""
    
    print(f"元の文字列:{str_arg}")
    
    #暗号化
    for idx,character in enumerate(str_arg):
        if(character.islower()):
            encrypted+=(chr(219-ord(character)))
        else:
            encrypted+=(character)
            
    print(f"暗号化結果:{encrypted}")
            
    #復号化
    for idx,character in enumerate(encrypted):
        
        #unicodeでは0x61(97)～0x7A(219)までが小文字→小文字は暗号化しても小文字のまま
        if(character.islower()):
            decrypted+=(chr(219-ord(character)))
        else:
            decrypted+=(character)  
            
    print(f"復号化結果:{decrypted}")

cipher("I am Matsuno")


# In[2]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', q8.ipynb])


# In[ ]:




