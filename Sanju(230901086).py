#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['one','two','three'],columns=['a','b','c'])
print(df)


# In[11]:


df.to_excel("D:\Sanju.xlsx")
df.to_excel("D:\Sanju1.xlsx")


# In[9]:


df=pd.DataFrame([[10,20,30],[40,50,60],[70,80,90]],index=['four','five','six'],columns=['x','y','z'])
df.to_excel("D:\Sanju.xlsx",sheet_name="Sheet.1")


# In[12]:


df=pd.DataFrame([[6,7],[1,2]],index=['a','b'],columns=['x','y'])
df.to_excel("D:\Sanju1.xlsx",sheet_name="Sheet.1")


# In[13]:


df.to_excel("D:\Sanju2.xlsx")


# In[19]:


x=pd.read_excel("D:\Sanju.xlsx")
y=pd.read_excel("D:\Sanju1.xlsx")
z=pd.concat([x,y])
z.to_excel("D:\Sanju2.xlsx")


# In[1]:


import pandas as pd
df=pd.read_excel("D:\Sanju2.xlsx")
print(df)
print(list(df))
print(format(len(df)))


# In[ ]:




