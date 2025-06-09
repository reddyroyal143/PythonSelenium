#Ex1:

# def func(i,j):
#     print(i,j)
# func(10,20) #Positional arguments
# func(j=20,i=10)  #Keyword arguments

#Ex2: Default values are assigned to the positionl argumnts
# def fun(i,j=10):
#     print(i,j)
# fun(100,200)    #change default values
# fun(100)             #one argument, default will take

#Ex3: Keyword arguments

# def greetings(name,greetmsg):
#     print(greetmsg+" "+name)
# greetings(name='Jhon',greetmsg='Hello')
# greetings(greetmsg='Hello',name='Jhon')

#Ex4:
# def my_fun(a,b,c):
#     print(a,b,c)
# my_fun(10,20,30)
# my_fun(a=10,b=20,c=30)
# my_fun(10,20,c=30)
# my_fun(10,b=20,c=30)
# my_fun(10,b=20,30)      #Incorrect bcz positiona shold aper befor keyword arguments
# my_fun(10,20,b=30)      #Incorrect dueto logical error


#Ex5:
# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
# print(largest(100,200))
# print(largest(20,10))
#
# res=largest(10,20)
# print(res)
# print(type(res))











