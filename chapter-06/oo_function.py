#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

def if_print(x):
    if x :
        print '%s %s == True' %(x,repr(type(x)))
    else:
        print '%s %s == False' %(x,repr(type(x)))
#
#keyword function params
def print_params(title='Default',*p1,**p2):
    print title,p1,p2
#
print_params("abc",1,2,3,4,b=1,c=2)
print_params(1)
exit()

#keyword function
def func1(name,greeting="Hello"):
    print "%s ,%s !" %(greeting,name)
#
func1(greeting = 'Good night',name = "Heysion")
func1(name = "Heysion")
exit()
#keyword fib function
def fibs(num):
    'fib function'
    assert num > 2
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
#
print fibs(10)
print fibs.__doc__
print fibs(1)
exit()
#keyword callable
print callable(print_var)
x = 1
print callable(x)