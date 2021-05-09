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
