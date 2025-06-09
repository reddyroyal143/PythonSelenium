import sys
sys.path.append('C:/Users/royal/Desktop/Python/Day 9/packA')
sys.path.append('C:/Users/royal/Desktop/Python/Day 9/packB')

#Approach 1

# import emp
# empobj=emp.Employee(10,'john',20000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.Student(1122,'scott','B')
# stuobj.displaystu()

#Approach 2

from emp import *
empobj=Employee(10,'john',20000)
empobj.displayemp()

from stu import *
stuobj=Student(1122,'scott','B')
stuobj.displaystu()








