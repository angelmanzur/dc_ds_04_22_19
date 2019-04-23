#!/usr/bin/env python
# coding: utf-8

# # Dictionary

# In[28]:


mydict = {'A': [20.1, "AA"], 'B': [23.2,"BBB"], 'C':[5.4, "CCC"], 'D':[34.2,"DDD"], 'E':[33.5,"EEE"]}


# In[29]:


mydict


# In[31]:


mydict.pop('B')


# In[32]:


mydict


# In[33]:


mydict['A'][0] = 44.1


# In[34]:


mydict


# In[37]:


ages =[]
for entry in mydict:
    print(mydict[entry][1])
    ages.append(mydict[entry][0])
    


# In[38]:


ages


# In[ ]:




