#!/usr/bin/env python
# coding: utf-8

# In[16]:


file_path=r'C:\Users\priyanka\Desktop\python programs\New folder\Mall_Customers.txt'
fil=open(file_path,'r')
dic={}
ag1=1
ag2=19
dic2={}

#build dictiory with age groups for expl {(1, 19): [], (20, 39):[], (40, 59):[], (60, 79): []}
while ag2 <=80:
    t=ag1,ag2
    dic2[ag1,ag2]=[]
    ag1=ag2+1
    ag2=ag1+19

dic={}
for lin in fil:
    if lin[0].isalpha():
        continue
    
    col=lin.split(',')
    age,spd=int(col[2]),int(col[4])
    
    for grp in dic2.keys():
        if grp[0] <= age <= grp[1]:
            dic2[grp].append(spd)

#find group average
for grp in dic2:
    dic2[grp]=round(sum(dic2[grp])/len(dic2[grp]))


max_ag =(sorted(dic2.items(),key = lambda kv:kv[1],reverse=True)[0])
print(f'The age group having Max spending : {max_ag[0]} and averge spening is {max_ag[1]}')

fil.close()
print('End of Program')

    

        
        


# In[ ]:




