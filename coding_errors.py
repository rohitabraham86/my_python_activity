#!/usr/bin/env python
# coding: utf-8

# # Code 1

# In[1]:


# Print the price
sales_price = 24500

print(total_price)


# In[2]:


# corrected code
sales_price = 24500

print(sales_price)


# # Code 2

# In[3]:


# Print a text string verbatim
print "My name is James Bond"


# In[11]:


# Corrected Code
print("My name is James Bond") # functions should have paranthesis


# # Code 3

# In[6]:


# Determine if x is greater than 10
x = 11 

if x > 10:
print('X is greater than 10')
else: 
    print('x is not greater than 10')


# In[7]:


# Corrected Code
x = 11 

if x > 10:
    print('X is greater than 10') # if, else and where should have indentation
else: 
    print('x is not greater than 10')


# # Code 4

# In[8]:


# Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[11]


# In[10]:


# Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[5] # List items are indexed starting from 0. Here there are 6 items, so 'Hirsi' is indexed 5 and not 11

