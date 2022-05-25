#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 02: Evaluate the Summer Olympics, London 2012 dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: View and add the dataset

# In[1]:


#Import the necessary library
import numpy as np


# In[2]:


#Manually add the Summer Olympics, London 2012 dataset as arrays
country=np.array(["Great Britain","China","Russia","United States","Korea","Japan","Germany"])
country_gold=np.array([29,38,24,46,13,7,11])
country_silver=np.array([17,28,25,28,8,14,11])
country_bronze=np.array([19,22,32,29,7,17,14])


# #### Find the country with maximum gold medals

# In[4]:


#Use the argmax() method to find the highest number of gold medals
country_gold.argmax()


# In[5]:


#Print the name of the country
country[3]


# #### Find the countries with more than 20 gold medals

# In[12]:


#Use Boolean indexing technique to find the required output
print(country[country_gold>20])


# #### Evaluate the dataset and print the name of each country with its gold medals and total number of medals

# In[17]:


#Use a for loop to create the required output
for i in range(len(country)):
    gold_medals=country_gold[i]
    total_medals=country_gold[i]+country_silver[i]+country_bronze[i]
    print(f"{country[i]} has {country_gold[i]} gold medals among total number of {total_medals}")

