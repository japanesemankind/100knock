#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("q64_out.txt","r") as f:
    sem_cnt = 0
    sem_cor = 0
    syn_cnt = 0
    syn_cor = 0
    category=0
    for line in f:
        line = line.split()
        if (line[0]==":"):#カテゴリを示す行であれば
            
            #カテゴリを変更
            if(line[1].startswith("gram")):
                category=1
            else:
                category=0
                
        else:#それ以外の行について
            
            #カテゴリに基づき、意味的・文法的アナロジーの正解数、文の数をカウント
            if(category==0):
                sem_cnt+=1
                if line[3] == line[4]:
                    sem_cor += 1
            else:
                syn_cnt += 1
                if line[3] == line[4]:
                    syn_cor += 1

print(f"意味的アナロジー正解率: {sem_cor/sem_cnt}")
print(f"文法的アナロジー正解率: {syn_cor/syn_cnt}")


# In[ ]:




