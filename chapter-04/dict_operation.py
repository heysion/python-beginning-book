#
def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword dict setdefault update values itervalues
d = {}
d.setdefault('name',"N/A")
d.setdefault('age',-1)
print_var(d,"dict")
d['age'] = 10
print d.setdefault('age')
print d
x = {'url':"abc.com"}
d.update(x)
print d
print_var(d.values(),"dict")
it = d.itervalues()
print list(it)

exit()
#keyword dict keys iterkeys pop popitem
test = {'name':'ben','age':45,'url':"ben.com"}
print_var(test.keys(),"keys")
it = test.iterkeys()
print list(it)
print_var(test,"dict")
pop_ret = test.pop('url')
print_var(test,"dict")
print_var(pop_ret,"pop")
del pop_ret
pop_ret = test.popitem()
print_var(pop_ret,"pop")
print_var(test,"dict")


exit()
#keyword dict items iteritems
test = {'name':'ben','age':45,'url':"ben.com"}
print_var(test.items(),"item")
it = test.iteritems()
print_var(it,"it")
print list(it)

exit()
#keyword dict get has_key
name = {'name':'ben','age':45}
print name.get('name')
print name.get('abc')
print name.get('abc','Error')
print name.has_key('abc')
print name.has_key('name')
exit()
#keywrod dict copy deepcopy fromkeys
x = {"n":["abc","123"],"d":123}
print_var(x,"dict")
y = x.copy()
print_var(y,"dict")
print x == y
y['d'] = 999
print_var(x,"x dict")
print_var(y,"y dict")
y['n'].remove('123')
print_var(x,"x")
print_var(y,"y")
y.clear()
print_var(x,"x")
print_var(y,"y")
from copy import deepcopy
d = deepcopy(x)
print x == d
d['n'].remove('abc')
print_var(x,"x")
print_var(d,"d")
keys = ["name","age","lv"]
test = dict.fromkeys(keys)
print_var(test,"fromkeys")
del test
test = dict.fromkeys(keys,'Unknown')
print_var(test,"fromkeys")
exit()
#keywword dict clear
d = {}
print_var(d,"dict")
d['name'] = "Ben"
d['age'] = 45
print_var(d,"dict")
ret = d.clear()
print_var(d,"dict")
print_var(ret,"ret")

exit()
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