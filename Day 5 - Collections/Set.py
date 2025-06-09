#Ex1 : Creating Set
# myset={'apple','banana','cherry'}
# print(myset)
from os import remove

#Ex2 : Accessing items/values from set
# myset={'apple','banana','cherry'}
# for i in myset:
#     print(i)

#Ex 3 : value exist in set or not
# myset={'apple','banana','cherry'}
# print('banana' in myset)
# print('banan2a' in myset)

#Ex4 : Adding items to set
# add()-adds single item at a time     update()- adds multiple items
# myset={'apple','banana','cherry'}
# # myset.add('orange')
# myset.update(['mango','grapes'])
# print(myset)

#Ex5: Find no of items in a set
# myset={'apple','banana','cherry'}
# print(len(myset))

#Ex6: Remove items from set
#remove() discard()
# myset={'apple','banana','cherry'}
# myset.remove("banana")
# print(myset)
# myset.remove('jkl') #Keyerror
#
# myset.discard('banana')
# print(myset)
# myset.discard('klj') #will not throw any error


#Ex7: clear all items from the set
# myset={'apple','banana','cherry'}
# myset.clear()
# print(myset)
# del myset
# print(myset)

#Ex8: join two sets
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)

#Update()
set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1)



















