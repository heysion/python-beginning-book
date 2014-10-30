#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

def if_print(x):
    if x :
        print '%s %s == True' %(x,repr(type(x)))
    else:
        print '%s %s == False' %(x,repr(type(x)))
#
#keyword function recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#
print factorial(3)
print factorial(10)

def MyPower(x,n):
    result = 1
    for i in range(n):
        result = result * x
    return result
#
print MyPower(10,2)

exit()
#keyword function in function
def foo(x):
    def p(x):
        print "%s" %(repr(type(x)))
    return p(x)
#
foo(x=10)
def fobb(x):
    def foaa(x):
        return x*x
    return foaa(x)
#
print fobb(10)
exit()
#keyword var global local
def foo():
    global x
    x = x + 1
#
x = 10
foo()
print x
exit()
def foo(): x = 42 ; print x
x = 10
foo()
print x

exit()
#keyword function struct params
def add(x,y):
    return x+y
#
p1 = (1,2)
print_var(p1,"tuple")
print add(*p1)
p2 = {"x":1,"y":2}
print_var(p2,"list")
print add(**p2)
exit()
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