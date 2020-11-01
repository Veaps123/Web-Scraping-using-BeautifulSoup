#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[3]:


get_ipython().system('pip install bs4')


# In[11]:


get_ipython().system('pip install lxml')
from lxml import html


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


r = requests.get('https://news.ycombinator.com/')


# In[7]:


#check the page exit or not
if r.status_code == 200:
    html_data = r.text
    print(html_data)


# In[8]:


soup = BeautifulSoup(html_data,'html.parser')
print(soup)


# In[9]:


print(soup.prettify)


# In[34]:


tag1 = soup.findAll("a",href_="https://aphyr.com/posts/340-reversing-the-technical-interview")


# In[36]:


tag2 = soup.findAll("span",class_ = "score")


# In[40]:


tag3 = soup.findall("a",href_ = "item?id=24737171")


# In[ ]:




