#

def print_var(div,var):
    print "%s = %s  %s" %(str(var),repr(div),repr(type(div)))

#keyword list
name = list("Hello python v2.7")
print_var(name,"name")
print name.sort()
print_var(name,"name")

exit()


a = [1,2,3]
b = [4,5,6]
print_var(a+b,"a+b")
print_var(a,"a")
print_var(b,"b")
a.extend(b)
print_var(a,"a")
print_var(b,"b")
print a.index(4)
#print a.index(7)
b.insert(1,7)
print b.index(7)
print b
print b.pop()
print b
print b.remove(7)
print b
print b.reverse()
print b

exit()
name = list("Hello python v2.7")
print_var(name,"name")
name[6:] = list("heysion")
print_var(name,"name")
name.append(2014)
print_var(name,"name")
print name.count('o')


exit()
list_num=['1']
for i in range(10):
    str_temp = str((i+1)*7) * (i+1)
    list_num.append(str_temp)

print len(list_num)
print max(list_num)
print min(list_num)

exit()

database =[['alex',55],['wension',77],['daive',78],['jones',99]]
username = raw_input("username:")
pin = raw_input("pin code:")
print_var(username,"username")
print_var(pin,"pin")
if [username,int(pin)] in database:
    print "Access success"
else:
    print "Not Found!"

exit()
list_values = [1,2,3,4,5,6]
print 1 in list_values
print 7 in list_values

exit()

list_num = [1,2,3] + [4,5,6]
print_var(list_num,"list+list")
list_num = list_num * 3
print_var(list_num,"list*3")

exit(0)
number=['0']
for i in range(10):
    str_temp = str(i*10) * i
    number.append(str_temp)
#print number

print_var(number[3:6],"list[3:6]")
print_var(number[1:-1:2],"list[1:-1:2]")
print_var(number[-3:-1],"list[-3:-1]")
print_var(number[-3:],"list[-3:]")
print_var(number[::2],"list[::2]")

exit(0)
alex_info = ['alex zoo',55,'M']
rose_info = ['rose steven',18,'F']
print_var(alex_info,"list")
database = [alex_info,rose_info]
print_var(database,"list")

greeting = "Hello"
print_var(greeting[0],"list[0]")
print_var(greeting[-1],"list[-1]")
print_var(greeting[0:],"list[0:]")
print_var(greeting[:-1],"list[:-1]")
print_var(greeting[0],"list[0]")
print_var(greeting[3:-1],"list[3:-1]")

exit(0)
fourth = raw_input("year:")[3]
print_var(fourth,"input")

