
class ObjectBird:
    def __init__(self):
        pass
    #
    def say_greet(self,greeting):
        pass
    #
#
class FlyBird(ObjectBird):
    def __init__(self):
        pass
    def setGreet(self,greeting):
        self.greeting = greeting
        pass
    #
#
print issubclass(FlyBird,ObjectBird)
print issubclass(ObjectBird,FlyBird)
print '==========================='
b1 = ObjectBird()
b2 = FlyBird()
print isinstance(b1,ObjectBird)
print isinstance(b1,FlyBird)
print isinstance(b2,ObjectBird)
print isinstance(b2,FlyBird)
