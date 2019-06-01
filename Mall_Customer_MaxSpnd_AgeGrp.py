'''
Find which Age Group spend more.
Assumption - Age group having highest spending ratio spends more
'''

file_path=r'C:\Users\priyanka\Desktop\python programs\New folder\Mall_Customers.txt'
fil=open(file_path,'r')
dic={}
for lin in fil:
    if lin[0].isalpha():
        continue
    
    col=lin.split(',')
    age,spd=int(col[2]),int(col[4])
    if age in dic:
        dic[age].append(spd) 
    else:
        dic[age]=[spd]
for age in dic:
    dic[age]=sum(dic[age])/len(dic[age]) #this dictionary has age,avergae spending of the age

ag1=1
ag2=19
dic2={}
while ag2 <=80:
    t=ag1,ag2
    dic2[ag1,ag2]=[]
    for age in dic:
        if ag1 <= age <= ag2:
            dic2[ag1,ag2].append(dic[age])
        
    ag1=ag2+1
    ag2=ag1+19
for ag1,ag2 in dic2:
        if len(dic2[ag1,ag2]) > 0:
            dic2[ag1,ag2]=round(sum(dic2[ag1,ag2])//len(dic2[ag1,ag2])) #dic2 has age group range and their max spending

max_ag =(sorted(dic2.items(),key = lambda kv:kv[1],reverse=True)[0])
print(f'The age group having Max spending : {max_ag[0]} and averge spening is {max_ag[1]}')

fil.close()
print('End of Program')


