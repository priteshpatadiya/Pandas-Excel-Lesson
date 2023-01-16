#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("E:\Study material\Data since\gapminder-FiveYearData.csv")


# In[3]:


df


# In[4]:


print(df.loc[0])


# In[5]:


print(df.loc[99])


# In[6]:


print(df.tail(n=1))


# In[7]:


print(df.loc[[0,99,999]])


# In[8]:


print(df.iloc[1])


# In[9]:


print(df.iloc[-1])


# In[10]:


print(df.iloc[[0,99,999]])


# In[11]:


subset=df.loc[:,['year','pop']]


# In[12]:


print(subset.head())


# In[13]:


subset=df.iloc[:,[2,4,-1]]


# In[14]:


print(subset.head())


# In[15]:


small_range = list(range(5))


# In[16]:


print(small_range)


# In[17]:


subset = df.iloc[:,small_range]


# In[18]:


print(subset.head())


# In[19]:


print(df.loc[42,'country'])


# In[20]:


print(df.iloc[42,0])


# In[21]:


print(df.iloc[[0,99,999],[0,3,5]])


# In[22]:


#group bnana year,life exp nd year ke according mean life exp. ka
print(df.groupby('year')['lifeExp'].mean())


# In[23]:


#multi group ka mean(mean wali value ke liye[]me)
multi_group = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()


# In[24]:


print(multi_group)


# In[25]:


print(df.head())


# In[26]:


print(df.tail())


# In[ ]:




