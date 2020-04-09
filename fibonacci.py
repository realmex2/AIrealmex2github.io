#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("terms upto"))
a=0
b=1
c=0

for i in range(2,n): 
            c = a + b 
            a = b 
            b = c
            print(c)


# In[ ]:





# In[ ]:




