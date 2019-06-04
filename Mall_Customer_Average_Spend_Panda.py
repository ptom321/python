#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Program to find average spending score of Male and Female Customer Respectively
'''
import pandas as pd

url=r'https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2025%20-%20Hierarchical%20Clustering/Mall_Customers.csv'

df=pd.read_csv(url)

male_scor=df[df['Genre'] == 'Male']['Spending Score (1-100)'].mean()
female_scor=df[df['Genre'] == 'Female']['Spending Score (1-100)'].mean()

print(f'Average spending score male is {round(male_scor)}\nAverage spending score male is {round(female_scor)}')


# In[ ]:




