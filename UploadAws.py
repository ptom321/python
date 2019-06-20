#!/usr/bin/env python
# coding: utf-8

# In[7]:


import boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
s3_resource.Object('ptom321','reverse.txt').upload_file('reverse.txt')
print('done')

