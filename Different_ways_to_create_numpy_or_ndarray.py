#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creating numpy/n-d arrays array using different-2 ways
import numpy as np


# In[6]:


arr1=np.array([1,2,3,4,5])#1-d array
print(arr1)
arr1


# In[7]:


type(arr1) #it is telling that it(arr1) is an object of type ndrray of library numpy


# In[11]:


#2-d array
arr2=np.array([[1,2,3,4,5],[6,5,4,3,2]])
print(arr2)
arr2


# In[12]:


arr3=np.zeros((2,3))  #2nd way way to create an n-d array every value is zero
                      #if want to intialise array then we can use it
print(arr3)
arr3


# In[16]:


arr4=np.ones((3,3))  #2nd way way to create an n-d array every value is ones
                      #if want to intialise array then we can use it
print(arr3)           #datatype of values will be float
arr3


# In[14]:


type(arr3)


# In[15]:


type(arr3[0][0]) #you can see it here the type of value


# In[18]:


arr5=np.identity(4)
print(arr5)   
arr5                         #to create 2-d array like identity matrix


# In[23]:


arr6=np.arange(10) #arange generate an array from 0 to n-1 
                   #just like range function in for generate a list from 0 to n-1
print(arr6)
arr7 =np.arange(5,10)# 5 to 9
print(arr7)

arr8 = np.arange(5,15,3)# if we want to jump or gap from one number to another number
print(arr8)


# In[27]:


arr9= np.linspace(10,20,10) #it generate an array which is linearly spaced means the difference between to number will be same 
print(arr9) #means create an array of including 10 and 20 last 10 is number of values in that array


arr10= np.linspace(0,9,4) 
print(arr10)


# In[29]:


arr11= np.copy(arr10) #to copy array from one to another
print(arr11)


# In[ ]:




