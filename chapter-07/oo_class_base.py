
__metaclass__ = type
class Person:
    def __init__(self,name=None,greeting=None):
        if name is not None:
            self.name = name
        if greeting is not None:
            self.greeting = greeting
        pass
    #
    def setName(self,name):
        self.name = name
        pass
    #
    def getName(self):
        return self.name
        pass
    #
    def setGreet(self,greeting):
        self.greeting = greeting
    #
    def greet(self):
        print "%s, %s !" %(self.greeting,self.name)
    #
#
foo = Person()
foo.setGreet("Hello")
foo.setName("Heysion")
foo.greet()
f2 = Person(name = "Heysion")
f2.setGreet("Good night")
f2.greet()
f3 = Person(name="Heysion",greeting="Hello")
f3.greet()
f3.setGreet("Good Night")
f3.greet()
f2.greet()