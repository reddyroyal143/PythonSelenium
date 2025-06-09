#EX 1: creating a list


# mylist1 = [10,20,30,40,50]
# mylist2 = ['apple','banana','cherry']
# mylist3 = ['apple',10,'banana',20]
# mylist = list() #empty list
#
# print(mylist1)

#Ex2: Accessing items from the list

# mylist = ['apple','banana','cherry']
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

#Ex3: Range of indexes

mylist = ['apple','banana','cherry','orange','kiwi','melon','mango']
print(mylist[2:5])
print(mylist[-4:-1])

#Ex4: change item value

# mylist=['apple','banana','cherry']
# print(mylist)
# mylist[0]='orange'
# print(mylist)

#Ex5: read list items using loop statement

# mylist=['apple','banana','cherry']
# for i in mylist:
#     print(i)

#Ex6: check theitems is exist in the list or not

# mylist=['apple','banana','cherry']
# if 'cherry' in mylist:
#     print('present')
# else:
#     print('no')

#Ex:7 Counting no of items in a list

# mylist=['apple','banana','cherry']
# print(len(mylist))

#Ex8: Add new item in the list- append() and insert()

# mylist=['apple','banana','cherry']
# #mylist.append('orange')  #append() insert at end
# mylist.insert(1,"orange") #insert() will add anywhere
# print(mylist)

#Ex9: Remove item from list  {{Functions have () but keyword is just word}}

#pop()
# mylist=['apple','banana','cherry']
# # mylist.pop(0)
# print(mylist)

#del
# mylist=['apple','banana','cherry']
# del mylist[2]
# print(mylist)

#clear()
# mylist=['apple','banana','cherry']
# mylist.clear()
# print(mylist)

#Ex10: copy list

#list()
# mylist=['apple','banana','cherry']
# mylist2=list(mylist)
# print(mylist)
# print(mylist2)

#copy()
# mylist=['apple','banana','cherry']
# mylist2=mylist.copy()
# print(mylist)
# print(mylist2)

#Ex11: combine/join two lists

#Using + operator

list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)

#using looping statement

list1=['a','b','c']
list2=[1,2,3]
for i in list2:
    list1.append(i)
print(list1)

#using extend function

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)

#Ex12: compare
list1=['a','b','c']
list2=[1,2,3]

if list1==list2:
    print("Equal")
else:
    print("Not Equal")



























