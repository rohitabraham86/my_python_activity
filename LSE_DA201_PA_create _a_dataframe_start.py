#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Create a DataFrame from the dictionary

# **This is the start to the activity.**
# 
# A peer has come to you for help. They have started building a dictionary using Jupyter Notebook. Below you will find their incomplete code. Now that you have learned to add values and keys using a DataFrame, make changes to the code to complete the following:
# - Import the dictionary into a DataFrame and add two more rows to the state and capital columns.
# - Sense-check the code that was presented to you is accurate and free from errors.

# ### Raw data
# - states = ["Acre", "Alogoas", "Amapa", "Amazonas", "Bahia", "Ceara", "Distrito Federal", 
#             "Espirito Santo", "Goiás", "Maranhao", "Mato grosso", "Mato grosso do sul", 
#             "Minas gerais", "Para", "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro", 
#             "Rio Grande do norte", "Rio Grande do Sul", "Rondonia", "Roraima", "Santa Catarina", 
#             "Sao Paulo", "Sergipe", "Tocantins"]
# 
# - capitals = ["Rio Branco", "Maceió" "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", 
#               "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande","Belo Horizonte","Belém",
#               "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", 
#               "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

# ### Incomplete Dictionary

# In[3]:


import pandas as pd


# In[5]:


# Create dictionary
brazil = {'states' : ["Acre", "Alogoas", "Amapa", "Amazonas", "Bahia", "Ceara", "Distrito Federal",
                        "Espirito Santo", "Goiás", "Maranhao", "Mato grosso", "Mato grosso do sul", 
                        "Minas gerais", "Para", "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro", 
                        "Rio Grande do norte", "Rio Grande do Sul", "Rondonia", "Roraima", "Santa Catarina", 
                        "Sao Paulo", "Sergipe", "Tocantins"],
           'capitals' : ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", 
                         "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande","Belo Horizonte","Belém",
                         "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", 
                         "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]}

# Create data frame from dictionary
brazil_fire = pd.DataFrame(brazil)

# View the dataframe
brazil_fire


# In[6]:


# Adding 2 extra states & capital

brazil_extra = {'states' : ["state1", "state2"],
                'capitals' : ["cap1", "cap2"]
               }

brazil_fire_extra = pd.DataFrame(brazil_extra)
brazil_fire_extra


# In[7]:


# Concatinating the 2 data frames

brazil_fire_final = pd.concat([brazil_fire, brazil_fire_extra], ignore_index = True)

# View the concatinated dataframe
brazil_fire_final

