#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Create a dictionary for the emergency number.
dict_1 = {'123' : 'Law Enforcement',
                '224' : 'Fire and Rescue Services',
                '101' : 'Emergency Medical Services',
                '999' : 'Emergency Management',
                '900' : 'Public Works'}

emergency_num = pd.Series(dict_1)

print(emergency_num)


# In[6]:


# Create a dictionary for the emergency protocol. Prevention, mitigation, preparedness, response, and recovery
dict_2 = {'1' : 'Prevention',
         '2' : 'mitigation',
         '3' : 'preparedness',
         '4' : 'response',
         '5' : 'recovery'}

emergency_proto = pd.Series(dict_2)
print(emergency_proto)


# In[8]:


# Check carotid pulse (neck), breathing (nose), obstructions (nose, ears, mouth),
# pupils (responsive), consciousness, contact details, and allergies.
# Create a dictionary for the emergency checklist.
dict_3 = {'1' : 'Check carotid pulse (neck)',
         '2' : 'breathing (nose)',
         '3' : 'obstructions (nose, ears, mouth)',
         '4' : 'pupils (responsive)',
         '5' : 'consciousness',
         '6' : 'contact details',
         '7' : 'allergies'}

emergency_ckl = pd.Series(dict_3)
print(emergency_ckl)

