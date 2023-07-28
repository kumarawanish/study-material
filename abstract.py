from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show(self):
        pass

    def get_details(self):
        return f"My name is {self.name} age is {self.age}"
    
    

class Derived(AbstractClass):

    @property
    def show(self):
        return f"{self.name}"


b = Derived("Amit", 29)

b.name = "Rahul Singh"

print(b.get_details())
