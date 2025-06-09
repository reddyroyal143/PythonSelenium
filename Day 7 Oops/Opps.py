#Ex1:
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc=MyClass()
# mc.myfun()
# mc.display("Scott")

#Ex2:
# class myclass:
#     def m1(self):
#         print('This is instance method')
#     @staticmethod   #Annotation
#     def m2(self,num): #Self should also need a parameter in static method
#         print(self,num)
#
# mc=myclass()
# mc.m1()
# mc.m2(100,200)
# myclass.m2(100,20) #calling the static method through class not through object

#Ex3:
# class myclass:
#     a,b=10,20       #calss variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=myclass()
# mc.add()
# mc.mul()

#Ex4:
# i,j=15,25
# class myclass:
#     a,b=10,20
#     def add(self,x,y):          #x,y are local variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# mc=myclass()
# mc.add(1,2)

#Ex5:  accesing different variables with same name
# a,b=15,25
# class myclass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)      #local
#         print(self.a+self.b) #class variables
#         print(globals()['a']+globals()['b']) #global variables
#
# mc=myclass()
# mc.add(1,2)

#Ex6: one class can have multiple objects

# class myclass():
#     def display(self,name):
#         print("This is display method")
#         print(name)
# obj1=myclass()
# obj1.display('Jhon')
#
# obj2=myclass()
# obj2.display('Scot')

#Ex7: Constructor

# class myclass():
#     def __init__(self):
#         print('This is construuctor')
#     def m1(self):
#         print('hello')
#     def m2(self,x,y):
#         return (x+y)
# mc=myclass()            #Invoked constructoer automatically
# mc.m1()                 #method have to call explicitly by using an object
# res=mc.m2(10,20)
# print(res)

#Ex8:

# class mycalss:
#     name='john'
#     def __init__(self,name): #constructor expecting argument
#         print(name)
#         print(self.name)
# mc=mycalss('David')             #passing parameter to thr constructor

#Ex9:
#Req: Emp
# constructor: eid, ename, sal
#display() : print eid, ename & sal

# class Emp:
#     def __init__ (self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101,"john",500000)
# e1.display() #101 john 500000
#
# e2=Emp(102,"scott",700000)
# e2.display() #102 scott 700000

#Ex10:
#Req: Emp
# constructor: eid, ename, sal
#display() : print eid, ename & sal

class Emp:
    def __init__ (self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):          #String Constructor
        return (self.ename)

e1=Emp(101,"john",500000)
print(e1)               #Printing the object will return data





















