#Ex:1

# class A:                #For class UPPER case and for variables LOWER case
#     def m1(self):
#         print('this is m1 method from class A')
# class B(A):
#     def m2(self):
#         print('this is m1 method from class B')
# bobj=B()
# bobj.m1()   #from A
# bobj.m2()   #from B

#Ex:2  Single Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
#         print(self.x + self.y)
# bobj=B()
# bobj.m1()
# bobj.m2()

#Ex3: Multi level inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Ex4: Hierarchy Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()
# bobj.m2()
#
# cobj=C()
# cobj.m1()
# cobj.m3()

#Ex5: Multiple Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Ex6:  Method Over Riding [Calling parent class from child class using super()]

# class A:
#     def m1(self):
#         print('This is m1 from class A')
#
# class B(A):
#     def m1(self):
#         print('This is m1 from class B')
#         super().m1()
#
# bobj=B()
# bobj.m1()

#Ex7:

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
#
# bobj=B()
# bobj.m(1000,2000)

#Ex8: Overriding variables

# class Parent:
#         name="Scott"
#
# class Child(Parent):
#     name = "John"
#     def test(self):
#         print(super().name)
#
# cobj=Child()
# print(cobj.name)
# cobj.test()

#Ex9: Overiding methods

# class Bank:
#     def rateOfIntrest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfIntrest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfIntrest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateOfIntrest())
#
# objy=YBank()
# print(objy.rateOfIntrest())

#Ex10: Overloading Concept(Ploymorphism)

# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print('Hello '+name)
#         else:
#             print('Hello')
#
# h=Human()
# h.sayHello()
# h.sayHello('Scott')

#Ex11: Overloading Concept(Ploymorphism)

# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# calobj=Calculation()
# calobj.add()
# calobj.add(10,20)
# calobj.add(10,20,30)



















