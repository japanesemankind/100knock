#!/usr/bin/env python
# coding: utf-8

# In[14]:


from q5 import q5 as n_gram

def q6(str_A,str_B,calc):
    set_A=set()
    set_B=set()
    for element in n_gram(str_A,2):
        set_A.add(element)
    for element in n_gram(str_B,2):
        set_B.add(element)
        
    if(calc=="&"):
        return set_A&set_B
    elif(calc=="-"):
        return set_A-set_B
    elif(calc=="|"):
        return set_A|set_B
    
in_X="paraparaparadise"
in_Y="paragraph"

#和集合
print(q6(in_X,in_Y,"|"))
#積集合
print(q6(in_X,in_Y,"&"))
#差集合X-Y
print(q6(in_X,in_Y,"-"))
#差集合Y-X
print(q6(in_Y,in_X,"-"))

if "se" in n_gram(in_X,2):
    print("X中にseは存在する")
else:
    print("Y中にseは存在しない")
if "se" in n_gram(in_Y,2):
    print("Y中にseは存在する")
else:
    print("Y中にseは存在しない")

