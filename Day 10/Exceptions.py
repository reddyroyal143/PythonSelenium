#Ex 1:

# print('start')
# print('start')
# try:
#     print(x)
# except:
#     print('Exception')
# print('end')

#Ex 2:
# print('Start')
# print('In Progress')
# try:
#     print(10/3)
# except ZeroDivisionError:
#     print('Handled')
# print('Completed')

#Ex 3: Multiple except blocks - try, except,else,finally
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print('result is: ',result)
# except ZeroDivisionError:
#     print('ZeroDivisionError Exception')
# except SyntaxError:
#     print('SyntaxError Exception')
# except:
#     print('Exception Handled')
# else:
#     print('No Exceptions Occured')
# finally:
#     print('Always Execute')


#Ex 4: raising own exceptions

def enterage(num):
    if num<0:
        raise ValueError('Only Integers are allowed')
    if num%2==0:
        print('Even')
    else:
        print('odd')

num=-1
try:
    enterage(num)
except ValueError:
    print('value error')
print('completed')
    



















