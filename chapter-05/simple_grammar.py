#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

def if_print(x):
    if x :
        print '%s %s == True' %(x,repr(type(x)))
    else:
        print '%s %s == False' %(x,repr(type(x)))
#
#keyword loop else
for n in range(10,0,-1):
    if n < 3:
        print n
        break
else:
    print 'else'
exit()
#keyword while True break
index = 0
while True:
    if index >10:
        break
    else:
        index = index + 1
        print index
exit()
#keyword range
print range(10,0,-1)
print range(0,10,2)
print range(0,10,1)
print range(1,10,2)
print range(9,0,-2)
exit()
#keyword loop break continue
for n in range(99,0,-1):
    if n < 10 :
        break
    else:
        print n
        continue
        print 1
exit()
#keyword sorted reversed
number = range(10)
print_var(number,"num")
print_var(sorted(number),"num")
number = reversed(number)
print_var(list(number),"num")
exit(0)
#keyword for enumerate
bstr = range(100)
for index , string in enumerate(bstr):
    if 15 == string:
        bstr[index]=105
print bstr
exit()
#keyword for zip
print_var(zip(range(3),range(3),range(3),range(30)),"zip")
names = ['x','y','z']
ages = [1,2,3]
test = [5,6,7]
for i in range(len(names)):
    print names[i],'is',ages[i]
print_var(zip(names,ages,test),"zip")
exit()
for x in range(10):
    print x
print range(5,10)
d = {'x':1,'y':2,'z':3}
for key in d:
    print key,"values ",d[key]
exit()
#keyword while
x = 1
while x <= 100:
    print x
    x += 1
exit()

#keyword assert
age = 10
assert 0 < age < 100
age = -1
assert 0 < age < 100
exit()
#keyword is
x = y = [1,2,3]
z = [1,2,3]
print x == y
print x is y
print x is z
print x == y
print x == y and x is z
print x == y or x is z
print x == y and not x is z
print x == y and not x == z
exit()
#keyword if elif
num = input("enter a number:")
if num > 0:
    print 'the number more zero'
elif num < 0:
    print 'the number less zero'
else:
    print 'the number is zero'

exit()

#keyword assignment
x, y, z = 1, 2, 3
print x, y, z
x, y = y, x
print x, y, z
test = {'name':"Ben",'age':45}
key, value = test.popitem()
print_var(key,"key")
print_var(value,"value")
print_var(test.items(),"item")
x = False
if_print(x)
del x
x = None
if_print(x)
del x
x = 0
if_print(x)
del x
x = ""
if_print(x)
del x
x = ()
if_print(x)
del x
x = []
if_print(x)
del x
x = {}
if_print(x)
print True + False + 42
#name, age = test.items()
#prnt_var(name,"name")
#print_var(age,"age")
exit()
#keyword import
#import somemodule
#from somemodule import somefunction
#from somemodule import function1,founction2
#from somemodule import *
import math as foobar
print foobar.sqrt(4)
from math import sqrt as MySqrt
print MySqrt(4)
exit()
#keyword print
print 'Age:',42
name = 'Ben'
age = 45
text = "Hello"
print text ,name ,age
exit()