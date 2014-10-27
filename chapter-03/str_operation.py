def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword string lower
name = "ABCd"
print name.lower()
print name.islower()
print name.capitalize()
print name.swapcase()
print name.title()
print name.istitle()
print name.upper()
print name.isupper()
print "that's all !'".title()
print "that's all !'".capitalize()
exit()
#keyword string join
seq = ['1','2','3','4','5']
print_var(seq,"list")
sep = '+'
print sep.join(seq)

name = 'abced'
print name.join('1')
dirs = '','usr','bin','env'
print_var(dirs,"list")
print '/'.join(dirs)

exit()
#keyword string find rfind rindex count startwith endwith
test = "abcd10000000000000000kjxkjkjlk"
print test.find('jk')
print test.find('9')
print 'j' in test
print 'jk' in test
print test.rfind('k')
print test.find('k')
print test.index('j')
print test.rindex('j')
print test.count('j')
print test.startswith('j')
print test.startswith('abcd')
print test.endswith('k')
print test.endswith('abc')

file_name = 'b.exe'
print file_name.endswith('.exe')

exit()
name = "abcd10000000000000000"
print name.isdigit()

exit()

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