# 1. Check given nmber is positive or negetive
# num=0
# print('positive') if num>=0 else print('Negetive')

#2. Check Largest of 2 numbers
# num1=3
# num2=1
# print(num1) if num1>num2 else print(num2)

#3. Check Largest of 3 numbers
# num1=6
# num2=1
# num3=2
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# elif num3>num1 and num3>num2:
#     print(num3)

#4.Provide wee number if you provide weekname as input
Str=input('Week is ')
Sunday=0
Monday=1
Tuesday=2
Wednesday=3
Thursday=4
Friday=5
Saturday=6

if Str=="Sunday":
    print(Sunday)
elif Str=='Monday':
    print(Monday)
elif Str=='Tuesday':
    print(Tuesday)
elif Str=='Wednesday':
    print(Wednesday)
elif Str=='Thursday':
    print(Thursday)
elif Str=='Friday':
    print(Friday)
elif Str=="Saturday":
    print(Saturday)
else:
    print("Invalid Input")

