#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

#  ## Helicopter Prison Escapes

# We begin by importing some helper functions

# In[1]:


from helper import *


# ## Get the Data

# Let's print the first 3 rows

# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)

for row in data[:3]:
    print(row)


# Removing the details

# In[3]:


index = 0
for row in data:
    data[index] = row[:-1]
    index +=1
print(data[:3])


# Extracting the year

# In[4]:


for row in data:
    row[0] = fetch_year(row[0])
print(row[0])


# The following also worked: 
# 
# for row in data:
#     date = fetch_year(row[0])
#     row[0] = date
# print(data[:3])

# Attempts per year

# In[5]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[6]:


years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# In[7]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# In[8]:


for row in data: # Instruction 1 - for each row in data
    for year_attempt in attempts_per_year: # Instruction 2 - nothing to do here
        # Instruction 3 - assign the year value in year_attempt to year
        year = year_attempt[0] 
        if row[0] == year:
            year_attempt[1] += 1
            
print(attempts_per_year)


# ### In which year did the most attempts at breaking out of prison with a helicopter occur

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot (attempts_per_year)


# The most prison breaks occurred 2009, 2007, 2001, and 1986

# ### In which countries do the most attempted helicopter prison escapes occur?

# In[10]:


countries_frequency = df["Country"].value_counts()

print_pretty_table(countries_fre)

