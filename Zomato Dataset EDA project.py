#!/usr/bin/env python
# coding: utf-8

# # Importing Required Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mat


# # Loading the dataset

# In[2]:


# giving the variable name:

data = pd.read_csv("C:/Users/dk957/Downloads/zomato.csv", encoding='ISO-8859-1')


# In[3]:


#loading the country_dataset and giving variable:

country_data = pd.read_excel("C:\\Users\\dk957\\Downloads\\Country-Code.xlsx")


# In[4]:


# Merging two datasets on comman column country code:

data = pd.merge(data,country_data,on="Country Code",how="left")


# In[5]:


#Setting up to show all columns of dataframe

pd.set_option("display.max_columns",None)


# In[6]:


#showing each column along with it's corresponding count of unique values

data.nunique()


# ## Plotting the null values heatmap:

# In[113]:


sns.heatmap(data.isna(), yticklabels = False,cmap='viridis',cbar=True)


# In[8]:


# Checking the count of unique values in Country column:
country_names = data.Country.value_counts().index
country_count = data.Country.value_counts().values


# ## Creating a pie chart to visualize countries with their counts:

# In[114]:


plt.pie(x=country_count[:3],labels=country_names[:3],autopct='%.1f%%')


# Observation:
# 1. Zomato has most number of transations from India(94.4%), United States(4.7%) and United Kingdom(0.9%)

# ## Grouping the data with rating columns to find out more relations:

# In[115]:


rating_count = data.groupby(["Aggregate rating","Rating color","Rating text"]).size().reset_index().rename(columns={0:"count"})

rating_count


# Observation:
# 1. 0.0 rating refers to no ratings given by customers
# 2. 1.8 to 2.4 rating referes to poor
# 3. 2.5 to 3.4 rating refers to average
# 4. 3.5 to 3.9 rating refers to good
# 5. 4.0 to 4.4 rating refers to very good
# 6. 4.5 to 4.9 rating refers to excellent

# In[116]:


#increasing the size of the plot:

mat.rcParams['figure.figsize'] = (12,6)


# ## Visualizing the count of each rating:

# In[117]:


sns.barplot(x=rating_count["Aggregate rating"],y=rating_count["count"],hue="Rating color",data=rating_count,palette=(["Blue","Red","Orange","Yellow","Green","Green"]))


# Observation:
# 1. 0.0 rating count is very high
# 2. Maximum number of ratings are between 2.5 to 3.4 belongs to Average

# ## Creating a countplot for each rating:

# In[119]:


sns.countplot(rating_count["Rating color"],data=rating_count,palette=(["Blue","Red","Orange","Yellow","Green","Green"]))


# In[60]:


## Finding the country names that have given 0 ratings:

country_zero_rating= data[data["Aggregate rating"]==0.0].reset_index().groupby(["Aggregate rating","Country"]).size().reset_index().rename(columns={0:"count"}).sort_values(["count"],ascending=False)

country_zero_rating


# In[64]:


#Visualizing the country counts with 0 rating:

sns.barplot(x=country_zero_rating["Country"],y=country_zero_rating["count"],data=country_zero_rating)


# Observation:
# 1. Most of the no ratings are given by Indian Customers.

# In[68]:


# Finding which currency is used by which country:

country_currency = data.groupby(["Country","Currency"]).size().reset_index().

country_currency


# In[73]:


# Finding out which countries have online deliveries:

country_online_delivery = data[data["Has Online delivery"]=="Yes"].groupby(["Country","Has Online delivery"]).size().reset_index().rename(columns={0:"count"})

country_online_delivery


# Observation:
# 1. Only India and UAE have Online Delivery Options

# In[91]:


#visualizing the transaction bases on city disytibution:

values=data["City"].value_counts().values
labels=data["City"].value_counts().index

plt.pie(x=values[:5],labels=labels[:5],autopct="%.2f%%")


# Observation:
# 1. Maximum number of transactions happened from Delhi (68.87%).

# In[97]:


# Finding the top 10 cusines:

top_10_cuisines = data[["Country","Cuisines"]].groupby("Cuisines").size().reset_index().rename(columns={0:"count"}).sort_values(["count"],ascending=False).head(10)

top_10_cuisines


# In[111]:


# Visualizing the top 10 Cusinies:


sns.barplot(x=top_10_cuisines["Cuisines"],y=top_10_cuisines["count"],data=top_10_cuisines)

#rotating x labels for better view:
plt.xticks(rotation=90)

plt.show()


# Observation:
# 1. Most famous cusine is North Indian

# # Conclusion:

# 1. Zomato has most number of transations from India(94.4%), United States(4.7%) and United Kingdom(0.9%):
#    Focus to implement the services in other countries is required to improve the business.
#    
# 2. 0.0 rating count is very high:
#    Sales and promotional team needs to motivate the customer to give their valuable rating.
# 
# 3. Maximum number of ratings are between 2.5 to 3.4 belongs to Average:
#    Needs to focus on service quality to improve the ratings.
# 
# 4. Most of the no ratings are given by Indian Customers:
#    Indian customer should be given special perks for providing their valuable rating.
# 
# 5. Only India and UAE have Online Delivery Options:
#    Online delivery options need to be provided in other countries in order to improve the business.
# 
# 6. Maximum number of transactions happened from Delhi (68.87%):
#    Number of transactions from a city also depends on it's population. However, it can be increased by providing more offers.
# 
# 7. Most famous cusine is North Indian:
#    More focus and food quality should be given to North Indian food, so it can become more famous.

# In[ ]:




