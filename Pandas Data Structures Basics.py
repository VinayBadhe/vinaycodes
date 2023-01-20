#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


v = pd.Series(['vinu',29])


# In[6]:


v


# In[7]:


v = pd.Series(data=['vinu',5], index=['Name','Age'])


# In[8]:


v


# In[9]:


t=pd.DataFrame(
{
    "Name": ['Vinay','Preetam','Tanvi'],
    "Age":['29','31','26'],
    "Status":['Single','Married','Married'],    
}
)
t


# In[10]:


f=pd.DataFrame(
data={
        "Age":["29","31","26"],
        "Status":["Single","Married","Married"],    
    },
index=["Vinay","Preetam","Tanvi"],
columns=["Age","Status"],
)
f


# In[11]:


d=pd.read_csv('C:/Users/Administrator/Downloads/IPL IMB381IPL2013.csv')


# In[12]:


d


# In[13]:


d.loc[127]


# In[14]:


d['SIXERS'].describe()


# In[15]:


d['SIXERS'].max()


# In[16]:


d['SIXERS'].min()


# In[17]:


d['SIXERS'].std()


# In[18]:


d['SIXERS'].hist()


# In[19]:


g=d['SOLD PRICE']
g


# In[20]:


g[g>g.mean()]


# In[21]:


g>g.mean()


# In[25]:


d.index


# In[24]:


d.values


# In[26]:


d[d['SOLD PRICE']>d['SOLD PRICE'].mean()]


# In[29]:


d['COUNTRY'].sample(frac=1,random_state=62).values


# In[30]:


d.columns


# In[41]:


d.drop(['AGE'],axis='columns').columns


# In[43]:


d.to_excel('C:/Users/Administrator/Downloads/d.xlsx', sheet_name='d', index=False)


# In[ ]:




