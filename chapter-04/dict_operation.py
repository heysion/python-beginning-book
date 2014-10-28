#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword dict format
phonebook = {"Ben":"9912","Alice":"2341","Deep":"3258"}
print_var(phonebook,"dict")
print "Ben's  phone number is %(Ben)s" % phonebook
print "Deep's  phone number is %(Deep)s" % phonebook
template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>
'''
data = {"title":"My Home Page","text":"Welcome to my home page!"}
print template % data
exit()
#keyword dict len
test = {'alex':123,'ben':99,'Deep':55}
print_var(test,"dict")
print len(test)
print 'alex' in test
print 'hey' in test
print 55 in test


exit()
#keyword dict
phonebook = {'Alex':"144444","Ben":"99234","Deep":"56565"}
print_var(phonebook,"dict")
print_var(phonebook['Ben'],"dict[item]")
items = [("name","Gray"),("age",42)]
d = dict(items)
print_var(d,"dict")

del d
d = dict(name = "Gray" , age = 42)
print_var(d,"dict")
del d
d = dict()
print_var(d,"dict")
t = tuple()
print_var(t,"tuple")
l = list()
print_var(l,"list")
s = str()
print_var(s,"str")
exit()