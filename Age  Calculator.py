#!/usr/bin/env python
# coding: utf-8

# In[6]:


from datetime import datetime

d = int(input("When is ur date of birth: "))
m = int(input("When is ur month of birth: "))
y = int(input("When is ur year of birth: "))

birth_date = datetime(y,m,d)
today = datetime(2023,1,1)
age= today - birth_date
days= age.days

print(f" On January 1st you turned {days} old")


# In[ ]:




