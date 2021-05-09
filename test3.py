#5
class Animal:
    def speak(self):
        print(I cant speak)
class Dog(Animal):
    def sound(self):
        print(But i say gaw gaw)
class Cat(Animal):
    def sound(self):
        print(But i say myau myau)
dog = Dog()
dog.speak()
dog.sound()

#6
class Encapsulation:
    __name = None
 
    def __init__(self, name):
        self.__name = name
 
    def get_name(self):
        return self.__name
 
 
a = Encapsulation('Aidai')
print(a.get_name())

#7
class Tomato(): 
    def type(self): 
       print("Vegetable") 
     def color(self):
       print("Red") 
class Apple(): 
     def type(self): 
       print("Fruit") 
     def color(self): 
       print("Red") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_tomato = Tomato() 
obj_apple = Apple() 
func(obj_tomato) 
func(obj_apple)

#8

from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")    
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
            
            
#9
class MarsRoverComp():
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance) # instantiating the base

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)


if __name__ == "__main__":
    z = MarsRover("mars_rover2", "till Mars", "ISRO")
    print(z.launch())
    print(z.get_maker())

#10

my_list = [14, 27, 230, 13]
 
my_iter = iter(my_list)
 
print(next(my_iter))
print(next(my_iter))
 
print(my_iter.__next__())
print(my_iter.__next__())
 
next(my_iter)

#11

[i for in range(10) if not i%3] == list(i for i in range(10) if not i%3)

#12
class Message(object):
    def message(self):
        return 'Hello World'
AnotherMessage = Message
print AnotherMessage().message()

#13
class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass(BaseClass, Mixin1, Mixin2):
    pass
#14
class Vehicle:
    """docstring"""
 
    def __init__(self):
        """Constructor"""
        pass
