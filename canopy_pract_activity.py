#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

movies = pd.read_excel('movies.xlsx')
ott = pd.read_csv('ott.csv')


# In[7]:


# Describing the movies data set
print(movies.shape)
print(movies.dtypes)
print(movies.head)
print(movies.tail)


# In[8]:


# Describing the ott data set
print(ott.shape)
print(ott.dtypes)
print(ott.head)
print(ott.tail)

