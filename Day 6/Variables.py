#Ex1:
# global_var=20   #golbal variable
#
# def func():
#     local_fun=10 #local variable
#     print(local_fun)
#     print(global_var)
# func()
# # print(local_var)  #invalid bcoz it is local variable
# print(global_var)   #Valid bcoz it is global variable

#Ex2:

# xy=100      #Golbal variable
# def cool():
#     xy=200
#     print(xy)
# cool()

#Ex3: Using global variable in local variable and update the value

# xy=100      #Golbal variable
# def cool():
#     global xy=200   #invalid statement
#     global xy
#     xy=200   #Global Variable
#     print(xy)
# cool()
#
# print(xy)

#Ex4:
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
# #cool()
# print(x)

#Ex5: we can specify the global variables inside the function
def cool():
    global x
    x=100
    print(x)
cool()
print(x)















