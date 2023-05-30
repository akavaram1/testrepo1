#!/usr/bin/env python
# coding: utf-8

# In[11]:


from IPython.core.display import HTML
print("The title is:")
HTML('<h1>Data Science Toolsand Ecosystem</h1> ')


# In[12]:


str="In this notebook, Data Science Tools andEcosystem are summarized."
print(str)


# In[15]:


print("Some of the popular languages that Data Scientists use are:")
HTML('<ol><li>SQL</li><li>R</li><li>Python</li></ol>')


# In[16]:


print("Some of the commonly used libraries used by Data Scientists include:")
HTML('<ol><li>numPy</li><li>Pandas</li><li>Matplotlib</li></ol>')


# In[31]:



import pandas as pd

df = pd.DataFrame({'Data Science Tools': ['Rstudio', 'Apache Hadoop', 'Apache Spark']})
    
print(df)  


# In[32]:


HTML('<h3>Below are a few examples of evaluating arithmetic expressions in Python</h3>' )


# In[34]:


print('This a simple arithmetic expression to mutiply then add integers')
import math
x=(3*4)+5
print(x)


# In[41]:


print('This will convert 200 minutes to hours by diving by 60')
import math
min=200
hour= min/60 
print(hour)
  


# In[47]:


print('List popular languages for data science')
HTML(' <b><ul> <li>SQL</li><li>R</li><li>Python</li></ul> </b>')


# In[58]:


HTML(<h2>Author</h2>)
print('akavaram sragvi')


# In[ ]:




