#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[46]:


df = pd.read_csv('co2_mm_mlo.txt',comment='#',header=None, delim_whitespace=True)


# In[47]:


df.head(16)


# How would you pick columns 0,1,3

# In[49]:


#df.loc[:,[0,1,3]] # call all
mydf = df.loc[:,[0,1,3]] # call all


# Change names of columns to year, month and CO2

# In[52]:


mydf.columns = ['year','month','CO2']
mydf.head()


# 

# In[54]:


for i in range(len(mydf)):
    
    if mydf['CO2'][i]==-99.99:
        
        mydf['CO2'][i] = np.nan


# Add a col 'Day' with the value 15 for all

# In[55]:


mydf['Day'] = 15;
mydf.head()


# Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it))

# In[56]:


import datetime


# In[57]:


dt = datetime.datetime(1958, 2,15)
dt


# In[58]:


mydf['year'] = mydf['year'].apply(str)
mydf['month'] = mydf['month'].apply(str)
mydf['Day'] = mydf['Day'].apply(str)
mydf.dtypes


# In[59]:


mydf['date'] = mydf['year'] +'-'+ mydf['month'] +'-'+ mydf['Day'] 
mydf.head(14)


# In[60]:


mydf['date'] = mydf['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))


# In[61]:


mydf.head()


# In[62]:


mydf.info()


# Drop the 'Day' column

# In[71]:


mydf = mydf.drop(columns=['Day'])


# In[72]:


mydf.head()


# use pandas groupby to print the yeaerly avg. of co2 per year.

# In[74]:


mydf.groupby('year').mean().head()


# In[75]:


mydf.head()


# Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)
# 
# 
# A: so we can do some analysis on our own

# In[100]:


myarr = np.array(mydf['CO2'].dropna())


# In[106]:


print(myarr.mean())
print(myarr.min())
print(myarr.std())


# Repeat step (3) but this time using the np.where command.

# In[80]:


df2 = pd.read_csv('co2_mm_mlo.txt',comment='#',header=None, delim_whitespace=True)


# In[85]:


df2.head()
mydf2 = 


# In[89]:


mydf2 = df2.loc[:,[0,1,3]] # call all
mydf2.columns = ['year','month','CO2']
mydf2.head()


# where command input is where(condition, retun if true, return if false)

# In[93]:


mydf2['CO2'] = np.where(mydf2['CO2']==-99.99, np.NaN,mydf2['CO2'])


# In[94]:


mydf2.head()


# In[ ]:




