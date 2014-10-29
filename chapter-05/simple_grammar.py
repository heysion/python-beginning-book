#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

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