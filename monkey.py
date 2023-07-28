class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"hello!!!{self.name}")


obj = MyClass(name = "Shani", age=27)


def getDetails(self):
    return f"Hi My name is {self.name} and my age is {self.age}"

MyClass.getDetails = getDetails

print(obj.getDetails())

