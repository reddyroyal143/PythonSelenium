#creating string variable

# s="welcome"
# s='welcome'
# s=str('welcome')
# s=str("welcome")

#creating empty string variables
# name=''
# name=""
# name=str()
#-------------------
# Mutable - can change the value of the variable
#Immutable - cannot change the value of the variable
#Strings are Immutable

# str1="welcome"
# print(id(str1))
#
# str1=str1+"to python"
# print(id(str1))

#if the value is changed after update it is mutable

#-----------------
# + and * with string
# str="welcome"
# print(str+' programming')
# print(str*10)

#---------------
#Slicing [] operator
#starting index is 0
#ending index is 1

# str='welcome'
# print(str[1:3])
# print(str[:6])
# print(str[2:])
# print(str[1:-1])
# print(str[1:-2])

#----------------
#ord() and chr()

# print(ord('a'))
# print(chr(97))

#-----------------
# max() min() len()

# print(max('abc'))
# print(min('abc'))
# print(len('abc'))

#---------------------
# in , not in operators - retuns true or flase

# s='welcome'
# print('come' in s)
# print('lome' in s)
#
# s='welcome'
# print('come' not in s)
# print('lome' not in s)

#-----------------------
#String comparison - use relational operators

print("tim" == "tie")
print("free" != "freedom")
print("arrow" > "aron")
print("right" >= "left")
print("teeth" <= "tee")
print("yellow" <= "fellow")
print("abc" > "")

#-----------------------
#Testing Strings - ture or false

s='welcome to python'
print(s.isalnum())
print('welcome'.isalpha())
print("first number".isidentifier())
print(s.islower())
print('WELCOME'.isupper())
print(' '.isspace())


#---------------------
#Searching for sub strings

s="welcome to python"
print(s.endswith("thon"))
print(s.startswith("good"))
print(s.find("come"))
print(s.find("become"))
print(s.count("o"))

#-----------------------
#converting string functions

s="String in PYTHON"
s1 = s.capitalize()
print(s1)
s2=s.title()
print(s2)
s3=s.lower()
print(s3)
s4=s.upper()
print(s4)
s5=s.swapcase()
print(s5)
s6=s.replace("in", "on")
print(s6)

#--------------------------
#Reverse a string
#method 1:
s='welcome'
rev_str=''
for i in s:
    rev_str=i+rev_str
print('reverse string is:', rev_str)

#method 2:
s='welcome'
rev_str=s[::-1]
print(rev_str)




























