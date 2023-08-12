#!/usr/bin/env python
# coding: utf-8

# In[27]:


from random import randint

random_number_to_guess = randint(1,20)

for n in range(0,3):
    guess = int(input("Enter your guess: "))
    if guess == random_number_to_guess:
        print("Correct")
        break
    else:
        print("Try again")
        
random_number_to_guess


# In[ ]:


# KUNAL SINGH 

