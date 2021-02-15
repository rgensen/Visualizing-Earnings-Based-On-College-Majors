#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')


# In[16]:


import pandas as pd

recent_grads = pd.read_csv('recent-grads.csv')

recent_grads.head(5)


# In[17]:


recent_grads.describe()


# In[18]:


raw_data_count = recent_grads.shape[0]


# In[19]:


recent_grads = recent_grads.dropna()


# In[21]:


cleaned_data_count = recent_grads.shape[0]

raw_data_count == cleaned_data_count


# In[22]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[24]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# In[25]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[26]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[27]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[28]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[29]:


recent_grads['Sample_size'].hist(bins=25, range=(0,5000))


# In[31]:


recent_grads['Employed'].hist(bins=25, range=(0,5000))


# In[33]:


recent_grads['Full_time'].hist(bins=25, range=(0,5000))


# In[37]:


recent_grads['ShareWomen'].hist(bins=25, range=(0,1))


# In[38]:


recent_grads['Unemployment_rate'].hist(bins=25, range=(0,1))


# In[40]:


recent_grads['Men'].hist(bins=25, range=(0,10000))


# In[41]:


recent_grads['Women'].hist(bins=25, range=(0,10000))


# In[45]:


from pandas.plotting import scatter_matrix


# In[46]:


scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(10,10))


# In[47]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[59]:


scatter_matrix(recent_grads[['Full_time', 'Median']], figsize=(10,10))


# In[56]:


recent_grads_pwm = recent_grads[['Major', 'ShareWomen']]
recent_grads_pwm[:5].plot.bar(x='Major', y='ShareWomen')

