#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn


# In[6]:


#Creating a simple array 
arr = np.array([4,6,7])


# In[7]:


arr


# In[8]:


#You can assign the method to a variables or don't
np.array([4,6,7])


# In[9]:


np.array([[4,5,6],[1,2,3],[4,8,9]])


# In[13]:


np.arange(2,100)   # from 2 to 100, except 100


# In[16]:


np.arange(1,100,3) #from 1 to 100 three by three


# In[28]:


np.linspace(1,100,5)  #1 to 100, 5 number but the distance between number is equal


# In[30]:


np.eye(4)    #4x4 matrix diagonal matrix


# In[34]:


np.zeros(4, dtype=int)


# In[35]:


np.ones(4, dtype=str)


# In[36]:


np.empty([2,2], dtype=int)


# In[37]:


np.empty_like([2,2])


# In[38]:


np.identity(4)     #identitity matrix


# In[40]:


x = [4,5,6,7,8]
np.asarray(x)


# In[68]:


y = [12,13,14,15,16]
list(np.concatenate([x,y]))    #concatenate method used for combine two different array


# In[70]:


new_form = np.arange(1,11)


# In[71]:


new_form


# In[72]:


new_form = np.append(new_form,6)        #append method used for add values end of the array


# In[73]:


new_form


# In[3]:


arr = np.random.randn(1,10)


# In[4]:


arr


# In[6]:


np.delete(arr,1,1)


# In[8]:


dizi = np.array([
    [1,2,3,4,5],
    [2,4,6,8,10],
    [1,3,5,7,9]
])


# In[9]:


dizi


# In[ ]:


#As you can see numpy has a bunch of methods ıf you interested take a look the numpy website for help...


# In[ ]:




