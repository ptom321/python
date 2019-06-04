#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Program to find which age group spends more and also age group wise average spending
'''

labels=['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79']
my_list=range(0,80,10)
def label(age):
    for index,i in enumerate(my_list):
        if age < i:
            return labels[index-1]
        if index == len(my_list) - 1:
            return labels[index]

url=r'https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2025%20-%20Hierarchical%20Clustering/Mall_Customers.csv'

import pandas as pd

df=pd.read_csv(url)

df['Age']=df['Age'].apply(label)

df2=df.groupby('Age')[['Spending Score (1-100)']].mean()
max_spend=df2.loc[df2['Spending Score (1-100)'].idxmax()]

print(f'The average spending of each age group!!\n{df2}\n')
print(f'The Age group spending Maximum is :\n{max_spend}')




# In[ ]:




