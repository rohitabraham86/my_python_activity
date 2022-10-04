#!/usr/bin/env python
# coding: utf-8

# ## Scenario - PA 3.1.5

# Mandisa Nkosi is actively pursuing a career in data analysis. 
# She has established a relationship with a political party that needs to decide 
# how best to invest its available advertising budget. Mandisa thinks she can 
# explore potential advertising avenues by analysing films that are available 
# on streaming platforms. She will use the movies_merge.xlsx and ott_merge.csv data sets.
# 
# The insights gained from the analysis will inform the campaign, 
# promotional materials, slogans, and language the political party will use 
# to reach potential voters. You’ll return to this analysis throughout the week. 

# ## Objective 

# To prepare your files and Jupyter Notebook for analysis:
# 
#     1. Import the CSV files into DataFrames.
#     2. View the DataFrames.
#     3. Describe the DataFrames to understand the structures and data types. 
#     4. Merge the two DataFrames into a single DataFrame.

# In[3]:


# Import the library.
import pandas as pd
import numpy as np


# In[4]:


# Import the datasets.
movies_merge = pd.read_excel('movies_merge.xlsx')
ott_merge = pd.read_csv('ott_merge.csv')


# In[5]:


# View the 'movies_merge' DataFrame.
print("Shape of the movies_merge df is, ",movies_merge.shape)
movies_merge.head()


# In[6]:


# View the 'ott_merge' DataFrame.
print("Shape of the ott_merge df is, ",ott_merge.shape)
ott_merge.head()


# In[7]:


# Describe the DataFrame
print("The data types for movies_merge are:\n",movies_merge.dtypes)
print("\nThe data types for ott_merge are:\n",ott_merge.dtypes)


# In[8]:


# Merge the DataFrame.
merged_data = pd.merge(movies_merge, ott_merge,
                      on='ID', how='left')

# View the merged_data
print("Shape of the merged_data df is, ",merged_data.shape)
print("\nThe data types for merged_data are:\n",merged_data.dtypes)
merged_data.head()


# In[9]:


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

# In[10]:


mo_gpby = merged_data.groupby('Year')[['Netflix']].agg('sum').reset_index()
mo_gpby[mo_gpby['Year']>=2012]


# ### 2. Determine what the average runtime is of movies released each year since 2012.

# In[11]:


mo_gpby = merged_data.groupby('Year')[['Runtime']].agg(['sum','mean']).reset_index()
mo_gpby[mo_gpby['Year']>=2012]


# ### 3. Determine what the best and worst reviews are that movies received on Rotten Tomatoes since 2012.

# In[12]:


mo_gpby = merged_data.groupby('Year')[['Rotten Tomatoes']].agg(['max','min']).reset_index()
mo_gpby[mo_gpby['Year']>=2012]


# ## Scenario
# 
# The political party is considering running advertisements with some provoking messages,
# but they need to ensure the content is suitable for the audiences watching the films. 
# The data Mandisa is working with includes content ratings (in the Age column) 
# that Mandisa can use to organise the DataFrame.
# 
# ## Objective
# 
# Your objective at this stage is to organise the data by:
# 
#     -the film release date and content rating
#     -the title of movies, the directors, and genres by content rating
#     -the title of movies, the released year, and the language by content rating
#     -Netflix screened movies based on language, runtime, and country
#     -the title of movies, specified language, potential runtime, and genres by content rating.
# 
# You’ll need to use the pivot() function to create pivot tables for each description. 
# More specifically, you’ll:
# 
#     -create a DataFrame for each description
#     -employ the pivot() function on the merged and original DataFrames
#     -specify the necessary parameters for the pivot() function.

# In[13]:


# the film release date and content rating.
merged_data.pivot(index='Title', columns='Age', values='Year')


# In[14]:


# the title of movies, the directors, and genres by content rating.
merged_data.pivot(index='Title', columns='Age', values=['Directors', 'Genres'])


# In[15]:


# the title of movies, the released year, and the language by content rating
merged_data.pivot(index='Title', columns='Age', values=['Year', 'Language'])


# In[16]:


# Netflix screened movies based on language, runtime, and country.
merged_data.pivot(index='Title', columns='Netflix', values=['Language', 'Runtime', 'Country'])


# In[17]:


# the title of movies, specified language, potential runtime, and genres by content rating.
merged_data.pivot(index='Title', columns='Age', values=['Language', 'Runtime', 'Genres'])


# ### 3.2.4 Practical activity: apply() function
# ## Scenario
# 
# The political party is now ready to buy advertising slots and has received 
# quotes from a broadcaster. The fee for running an ad is a flat rate per 10 seconds
# of advertisement, with a minimum purchase of 60 seconds of advertising time per film. 
# The broadcaster also has a promotional, reduced fee for ads run during any documentary film.
# 
# ## Objective
# To help the political party decide how they might best invest their budget,
# Mandisa will answer the following business questions:
# 
#     -What is the effect of adding 60 seconds (one minute) to each movie?
#     -Which movies are documentaries?
# 
# Your objective is to answer the posed questions by using the apply() 
# and/or applymap() functions depending on whether you’re working on a 
# Pandas Series or a Pandas DataFrame.

# #### Q1. What is the effect of adding 60 seconds (one minute) to each movie?

# In[19]:


# Create a subset
merged_data_new = merged_data[['ID', 'Title', 'Genres', 'Runtime']]

# View subset
merged_data_new.head()


# In[21]:


# Add 60 seconds / 1 minute to the runtime
merged_data_new.Runtime.add(1)


# #### Q2. Which movies are documentaries?

# In[22]:


# Create a column to specify if Documentary or Not Documenatary.
merged_data_new['Gen_doc'] = np.where(merged_data_new['Genres'].str.contains
                                      ('Documentary'),'Documentary', 'Not Documentary')

# View
merged_data_new


# In[28]:


# Determine the number of characters.
number_of_chars = merged_data_new.Gen_doc.apply(len)

# Creating new column 'Gen_doc_len' in the dataframe.
merged_data_new["Gen_doc_len"] = number_of_chars

#View Dataframe.
merged_data_new


# ### Challenge: 
# Think of a way to help the political party save money. 
# Mandisa suggests subtracting 6 seconds (0.01 minutes) from the 
# Runtime of all the movies, resulting in saving if they 
# limit the number of adverts during a movie. 

# In[29]:


# Create a Subset
merged_data_run_less = merged_data[['ID', 'Title', 'Genres', 'Runtime']]

# View
merged_data_run_less.head()


# In[31]:


# Sub 6 seconds(0.01minutes) from the runtime
merged_data_run_less.Runtime.subtract(0.01)

