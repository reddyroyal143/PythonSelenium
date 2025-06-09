# name='john'
# age=30
# sal=5000.50
name,age,sal= 'john',30,5000.50 #we can define in single line

#Approach 1
#print(name,age,sal) #we can use single line

#Approach 2
# print('Name is:',name)
# print('Name is:',age)
# print('Name is:',sal)

#Approach 3
#print('Name is:%s Age is:%d Salary is:%g'%(name,age,sal))

#Approach 4 {}
print('Name is:{} Age is:{} Salary is:{}'.format(name,age,sal))
print('Age is:{} Name is:{} Salary is:{}'.format(name,age,sal)) #variables should be in order


