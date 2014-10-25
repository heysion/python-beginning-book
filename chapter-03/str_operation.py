def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))
#keywor string format
format = "hello ,%s . wellcome to %s for your!"
values = ('Heysion','Python')
print format % values
del format
pi_length = 3#int(raw_input("input length:"))
format = "Pi with %%.%df" %(pi_length)
#print format
from math import pi
print format % pi

print "%010.4f" % pi

print "%-010s" %('Heysion')
print "%+010s" %('Heysion')
print "%.*s" % (5,'akdjlakjdflkajfdkjakjfklajsdlkfja')
print "% 05d" % 10
print  "%05d" % 10
exit()
#keyword string
website = 'http://www.heysion.net'
print_var(website,"str")
website[-3:] = 'com'
print_var(website[-3:],"str")