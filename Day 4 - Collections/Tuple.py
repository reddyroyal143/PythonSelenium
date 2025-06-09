#Ex1: crating Tuple
# mytuple=('apple','banana','cherry')
# print(mytuple)
#
# mytuple=()

#Ex2: Access Tuple Items
# mytuple=('apple','banana','cherry')
# print(mytuple[1])
# print(mytuple[-1])

#Ex3:Range of indexes
# mytuple = ('apple','banana','cherry','orange','kiwi','melon','mango')
# print(mytuple[2:5])
# print(mytuple[-4:-1])

#Ex4: Changing tuple items

#by default tuple doesnot allow to change valus bcoz it is immutable
#but there is a workaround
#tuple--->list(modify)--->tuple

# mytuple=('apple','banana','cherry')
# mylist=list(mytuple)
# mylist[0]='orange'
# mytuple=tuple(mylist)
# print(mytuple)

#Ex5: reading tple items using loop

# mytuple=('apple','banana','cherry')
# for i in mytuple:
#     print(i)

#Ex6: Searching if item exists

# mytuple=('apple','banana','cherry')
# if 'banana' in mytuple:
#     print('yes')
# else:
#     print('No')

#Ex7:total no of items -length
# mytuple=('apple','banana','cherry')
# print(len(mytuple))

#Ex8: Add new items to the tuple - Not Possible
# mytuple=('apple','banana','cherry')
# mytuple[0]='orange' #Type Error
# print(mytuple)

#Ex9: Copy tuple
# mytuple1=('apple','banana','cherry')
# mytuple2=mytuple1
# print(mytuple2)

#Ex10: removing items from tple- not possible
# mytuple=('apple','banana','cherry')
# #tuple.remove('apple') #invalid data
# del mytuple
# print(mytuple)

#Ex11: join/combine tuple
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# tuple3=tuple1+tuple2
# print(tuple3)

#Ex12: compare tuples
tuple1=(10,20,30)
tuple2=('a','b','c')
if tuple1==tuple2:
    print('equal')
else:
    print('Not Equal')










