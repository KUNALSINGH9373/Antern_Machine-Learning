#!/usr/bin/env python
# coding: utf-8

# 1. Sqaure pattern 

# In[7]:


n = int(input('Enter no. of rows: '))

for i in range(1, n+1):
    print("*"*n)


# In[17]:


# Geometrical Square

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


size = 5
print_square(size)


# 2. Hollow Sqaure pattern

# In[21]:


size = int(input("Enter a number: "))
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Right Triangle Star Pattern

# In[24]:


n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print("*"*i)


# 4. Mirrored Right Triangle Star Pattern

# In[32]:


n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()


# 5. Pyramid star pattern

# In[33]:


n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()


# 6. Inverted Pyramid star Pattern

# In[34]:


n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# In[ ]:




