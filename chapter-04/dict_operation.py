#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword
phonebook = {'Alex':"144444","Ben":"99234","Deep":"56565"}
print_var(phonebook,"dict")
print_var(phonebook['Ben'],"dict[item]")
items = [("name","Gray"),("age",42)]
d = dict(items)
print_var(d,"dict")

del d
d = dict(name = "Gray" , age = 42)
print_var(d,"dict")
exit()