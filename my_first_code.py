#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is my firt line of code.
print ('My name is Rohit Abraham')
print ('Date : 16/09/2022')


# # Program to Analyse Real Estate Data

# # Question 1: What is the Total Sales Price in December?

# In[6]:


# Assigning property IDs to its Sale Price
a = 45000
b = 23400
c = 67000
d = 34600
e = 12900

# Calculating Total Sales Price
total = a + b + c + d + e

# Output
print ('Total Sales Price =',total)


# # Question 2: What is the Average Sales Price in December?

# In[5]:


# Calculating Average Sales Price
avg = total / 5
print ('Average Sales Price =',avg)


# # Question 3: What is the Property Price for C?

# In[7]:


comm_c = 6500
# Property Price =  Sales Price - Commission
print ('Property Price for C =', c - comm_c)

