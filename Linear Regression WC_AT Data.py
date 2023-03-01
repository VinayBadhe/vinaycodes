#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


v=pd.read_csv('C:/Users/Administrator/Downloads/WC_AT.csv')


# In[3]:


v


# In[5]:


v.corr()


# In[6]:


import statsmodels.formula.api as smf


# In[7]:


model=smf.ols("AT~Waist",data=v).fit()


# In[8]:


model.params


# In[13]:


model.tvalues


# In[14]:


model.pvalues


# In[15]:


newdata=pd.Series([75,85,90,95])


# In[17]:


pred_data=pd.DataFrame(newdata,columns=['Waist'])


# In[18]:


model.predict(pred_data)


# In[ ]:




