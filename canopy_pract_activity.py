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


# In[9]:


list(movies)


# In[10]:


list(ott)


# ### Calculating the sum missing values in Age column

# In[11]:


movies['Age'].isnull().sum()


# ### Replacing missing values with 'Others' in columns: Age, Directors, Genres, Country, and Language.

# In[14]:


movies['Age'].fillna('Others', inplace = True)

# Checking if the missing values in Age column is replaced with Others
movies['Age'].isnull().sum()


# In[15]:


movies['Directors'].isnull().sum()


# In[16]:


movies['Directors'].fillna('Others', inplace = True)

# Checking if the missing values in Directors column is replaced with Others
movies['Directors'].isnull().sum()


# In[17]:


movies['Genres'].isnull().sum()


# In[18]:


movies['Genres'].fillna('Others', inplace = True)

# Checking if the missing values in Genres column is replaced with Others
movies['Genres'].isnull().sum()


# In[19]:


movies['Country'].isnull().sum()


# In[20]:


movies['Country'].fillna('Others', inplace = True)

# Checking if the missing values in Country column is replaced with Others
movies['Country'].isnull().sum()


# In[21]:


movies['Language'].isnull().sum()


# In[22]:


movies['Language'].fillna('Others', inplace = True)

# Checking if the missing values in Language column is replaced with Others
movies['Language'].isnull().sum()


# ### Convert the Rotten Tomatoes data type from object to integer.

# #### 1. First check if there is any missing values in Rotten Tomatoes

# In[27]:


movies['Rotten Tomatoes'].isnull().sum()


# In[30]:


# Replace missing value with the mean
movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(), inplace = True)

# Calculate missing values for Rotten Tomatoes.
movies['Rotten Tomatoes'].isnull().sum()


# In[25]:


# Check the date type of Rotten Tomatoes.
print(movies['Rotten Tomatoes'].dtypes)


# In[31]:


# Changing data type
movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].astype(object).astype(int)
print(movies['Rotten Tomatoes'].dtypes)


# #### 2. Check if there are mising values in IMDb

# In[33]:


movies['IMDb'].isnull().sum()


# In[34]:


# Replace missing value with the mean
movies['IMDb'].fillna(movies['IMDb'].mean(), inplace = True)

# Calculate missing values for IMDb.
movies['IMDb'].isnull().sum()

