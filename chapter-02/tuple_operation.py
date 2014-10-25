#
#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

print_var((1,2,3),"tuple")
print_var(3*(40+2,),"tuple")
tuple_num = (1,2,3,4)
print_var(tuple_num[1:-1],"tuple[1:-1]")
print 1 in tuple_num
print (1,2) in tuple_num
exit()