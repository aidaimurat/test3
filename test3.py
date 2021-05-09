#6
class Encapsulation:
    __name = None
 
    def __init__(self, name):
        self.__name = name
 
    def get_name(self):
        return self.__name
 
 
a = Encapsulation('Aidai')
print(a.get_name())

