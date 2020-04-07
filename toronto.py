#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np


# Web scraping

# In[32]:


data=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# Storing the table in a dataframe df1

# In[34]:


df1=data[0]
df1.head()


# df1.shape

# Deleting cells of Borough column having 'Not assigned'values

# In[36]:


df1['Borough'].replace('Not assigned', np.nan, inplace=True)


# In[37]:


df1.dropna(subset=['Borough'], inplace=True)


# Replacing  'NaN' vaalues in 'Neighborhood' column with the corresponding values of 'Borough' column

# In[38]:


df1.Neighborhood.fillna(df1.Borough, inplace=True)


# In[25]:


df1.head()


# Replacing values in 'Neighborhood' column separated by '/' with ','

# In[40]:


df1['Neighborhood'] = df1['Neighborhood'].str.replace('/', ',')


# In[41]:


df1.head()


# In[30]:


df1.shape

