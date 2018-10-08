
# coding: utf-8

# In[2]:


import requests


# In[3]:


import re


# In[4]:


import bs4


# In[9]:


data = requests.get("https://www.amazon.in/gp/help/customer/contact-us")


# In[10]:


data


# In[14]:


email = re.findall(r'([\d\w\.]+@[\d\w]+\.\.\w+)',data.text)


# In[15]:


print (email)

