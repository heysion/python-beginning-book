#

def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword match cmatch
import math
print_var(abs(10-77),"10-77")

print_var(math.ceil(10.99),"10.99")
print_var(math.ceil(10),"10")
print_var(math.floor(10.99),"10.99")
print_var(math.floor(10),"10")
print_var(math.sqrt(10),"sqrt10")
print_var(math.sqrt(9),"sqrt9")

exit(0)

#keyword string
str_hello = "Hello word!"
print_var(str_hello,"str")

del str_hello
str_hello = 'Hi'
print_var(str_hello,"str")

str_hello = 'Let\'s go'
print_var(str_hello,"str")

del str_hello
str_hello = "let's got"
print_var(str_hello,"str")

str_hello = "Hello "
str_word = "Word"
print_var(str_hello+str_word,"str")

print_var(str(1000L),"1000L")
print_var(repr(1000L),"1000L")

str_long = '''abcd10000000000000000agdc
kajdlkjadkfjad
sdkfjalskdfjaldsf
asjdlkfajdskflj
askdlfajslf'''


print_var(str_long,"str")

str_temp ='c:\\window'
print str_temp

del str_temp
str_temp = r'c:\window'
print str_temp

del str_temp
str_temp = u'Hello word!'
print_var(str_temp,"str")



exit(0)

#keyword raw_input
div = raw_input("x:=")
print_var(div,"x")
exit(0)

#keyword input
div = input("x:=")
print_var(div,"x")

exit(0)

#keyword chufa div
div_int = 1/2
print_var(div_int,"1/2")

div_float = 1.0/2
print_var(div_float,"1.0/2")

del div_float
div_float = 1/2.0
print_var(div_float,"1/2.0")

del div_float
div_float = 1.0/2.0
print_var(div_float,"1.0/2.0")

div_long = 1L/2L
print_var(div_long,"1L/2L")

del div_long
div_long = 1L/2
print_var(div_long,"1L/2")

del div_long
div_long = 1L/2.0
print_var(div_long,"1L/2.0")

#keyword zhengchu div
ndiv_int = 1//2
print_var(ndiv_int,"1//2")

del ndiv_int
ndiv_int = 10//3
print_var(ndiv_int,"10//3")

ndiv_float = 10.0//3
print_var(ndiv_float,"10.0//3")

ndiv_long = 10L//3
print_var(ndiv_long,"10L//3")

del ndiv_long
ndiv_long = 10L//2L
print_var(ndiv_long,"10L//2L")

#keyword quyu

ddiv_int = 10%3
print_var(ddiv_int,"10%3")

ddiv_float = 10.0%3
print_var(ddiv_float,"10.0%3")

del ddiv_float
ddiv_float = 10.0%5
print_var(ddiv_float,"10.0%5")

ddiv_long = 10L%5
print_var(ddiv_long,"10L%5")

del ddiv_long
ddiv_long = 10L%5L
print_var(ddiv_long,"10L%5L")

#keyword chengfang power
pow_int = 2**3
print_var(pow_int,"2**3")

pow_float = 2.0**3
print_var(pow_float,"2.0**3")

pow_long = 2L**3
print_var(pow_long,"2l**3")

del pow_int
pow_int = (-3)**2
print_var(pow_int,"(-3)**2")

del pow_int
pow_int = (-2)**3
print_var(pow_int,"(-2)**3")




