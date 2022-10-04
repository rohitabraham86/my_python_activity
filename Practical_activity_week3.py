#!/usr/bin/env python
# coding: utf-8

# ## Scenario

# Mandisa Nkosi is actively pursuing a career in data analysis. 
# She has established a relationship with a political party that needs to decide 
# how best to invest its available advertising budget. Mandisa thinks she can 
# explore potential advertising avenues by analysing films that are available 
# on streaming platforms. She will use the movies_merge.xlsx and ott_merge.csv data sets.
# 
# The insights gained from the analysis will inform the campaign, 
# promotional materials, slogans, and language the political party will use 
# to reach potential voters. You’ll return to this analysis throughout the week. 

# ## Objective - PA 3.1.5

# To prepare your files and Jupyter Notebook for analysis:
# 
#     1. Import the CSV files into DataFrames.
#     2. View the DataFrames.
#     3. Describe the DataFrames to understand the structures and data types. 
#     4. Merge the two DataFrames into a single DataFrame.

# In[1]:


# Import the library.
import pandas as pd


# In[2]:


# Import the datasets.
movies_merge = pd.read_excel('movies_merge.xlsx')
ott_merge = pd.read_csv('ott_merge.csv')


# In[6]:


# View the 'movies_merge' DataFrame.
print("Shape of the movies_merge df is, ",movies_merge.shape)
movies_merge.head()


# In[5]:


# View the 'ott_merge' DataFrame.
print("Shape of the ott_merge df is, ",ott_merge.shape)
ott_merge.head()


# In[9]:


# Describe the DataFrame
print("The data types for movies_merge are:\n",movies_merge.dtypes)
print("\nThe data types for ott_merge are:\n",ott_merge.dtypes)


# In[11]:


# Merge the DataFrame.
merged_data = pd.merge(movies_merge, ott_merge,
                      on='ID', how='left')

# View the merged_data
print("Shape of the merged_data df is, ",merged_data.shape)
print("\nThe data types for merged_data are:\n",merged_data.dtypes)
merged_data.head()


# In[13]:


# Concatenate the DataFrame.
concat_data = pd.concat([movies_merge, ott_merge], axis=0)

# View the concat_data
print("Shape of the concat_data df is, ",concat_data.shape)
print("\nThe data types for merged_data are:\n",concat_data.dtypes)
concat_data.head()


# When the concat function was used the duplicates were included in the final DataFrame,
# so the total rows are 33484. But the merge funtion takes care of the duplicates and
# so the total rows of the DataFrame is 16744. 

# ### Objective - PA 3.1.9 Use groupby() and aggregate() functions
# Use the groupby() and aggregate() functions on the merged DataFrame to:
# 
#     1. Determine how many films from each year (released from 2012 to the present) 
#        were watched on Netflix.
#     2. Determine what the average runtime is of movies released each year.
#     3. Determine what the best and worst reviews are that movies received 
#        on Rotten Tomatoes.

# ### 1. Determine how many films from each year (released from 2012 to the present) were watched on Netflix. 

# In[18]:


mo_gpby = merged_data.groupby('Year')[['Netflix']].agg('sum').reset_index()
mo_gpby[mo_gpby['Year']>=2012]


# ### 2. Determine what the average runtime is of movies released each year since 2012.

# In[23]:


mo_gpby = merged_data.groupby('Year')[['Runtime']].agg(['sum','mean']).reset_index()
mo_gpby[mo_gpby['Year']>=2012]


# ### 3. Determine what the best and worst reviews are that movies received on Rotten Tomatoes since 2012.

# In[24]:


mo_gpby = merged_data.groupby('Year')[['Rotten Tomatoes']].agg(['max','min']).reset_index()
mo_gpby[mo_gpby['Year']>=2012]

