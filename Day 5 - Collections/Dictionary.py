#Ex1 : Creating dictionary
# mydic={101:'x',102:'y',103:'z'}
# print(mydic)

#Ex2: Access items from dictionary
# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":"2021"
# }
# print(mydic["Brand"])
# print(mydic["Model"])
#
# #Using get()
# print(mydic.get("Model"))

#Ex3: Change values in dictionary
# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":"2021"
# }
#
# mydic["Year"]=2022
# print(mydic)

#Ex4: Reading items from dictionary using loop
# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":"2021"
# }

# for i in mydic:
#     print(i) #prints keys
# for i in mydic:
#     print(mydic[i]) #prints values
# for i in mydic.values():
#     print(i)
# for x,y in mydic.items():
#     print(x,y) #prints bot keys and values

#Ex5: Check key is exist or not

# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
# if "Model" in mydic:
#     print("exist")
# else:
#     print("Not Exist")
#
# print("Model" in mydic)


#Ex6: fin total no of items in dictionary

# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
# len=len(mydic)
# print(len)

#ex7: Adding items to dictonary

# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# mydic["Colour"]="red"
# print(mydic)

#Ex:Remove items from dic
# mydic={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
# mydic.pop("Year")
# print(mydic)

# del mydic["Year"]
# print(mydic)

# del mydic
# print(mydic)

# mydic.clear()
# print(mydic)

#Ex9: Copying Dictionary
# mydic1={
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
# mydic2=mydic1
# print(mydic2)   #Without using copy function

# mydic2=mydic1.copy()
# print(mydic2)     #With copy function













