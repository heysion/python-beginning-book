#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

def if_print(x):
    if x :
        print '%s %s == True' %(x,repr(type(x)))
    else:
        print '%s %s == False' %(x,repr(type(x)))


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