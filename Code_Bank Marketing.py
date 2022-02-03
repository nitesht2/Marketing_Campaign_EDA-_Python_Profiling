#!/usr/bin/env python
# coding: utf-8

# ## Bank Marketing Exploratory Data Analysis Using Python Profile

# In[30]:


import numpy as np
import pandas as pd


# In[32]:


#Reading the data set
data=pd.read_csv('bank.csv')
print(data.shape)


# In[33]:


#Exploring data
data.head()


# In[34]:


#To get the descriptive statistics
data.describe()


# In[ ]:


#install pandas-profiling

pip install pandas-profiling


# In[36]:


#import profilereport from pandas_profiling

from pandas_profiling import ProfileReport

#passing the data to the profile
profile = ProfileReport(data,title='Bank Marketing Campaign Model', html={'style' : {'full_width':True}})


# In[26]:


# Generting comprehensive output

profile


# In[27]:


#Generating output as html file. 
profile.to_file("Bank Marketing output.html")


# In[ ]:




