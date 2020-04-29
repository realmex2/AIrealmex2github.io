#!/usr/bin/env python
# coding: utf-8

# In[5]:


#ol(.OL
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


data=pd.read_csv('mnist_test.csv')


# In[8]:


data.head()


# In[9]:


a=data.iloc[3,1:].values


# In[14]:


a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[ ]:




