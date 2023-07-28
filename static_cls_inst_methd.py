class Person:

    count_instance = 0 # class variable
    def __init__(self, f_name, l_name, age, salary):
        Person.count_instance += 1
        self.fname= f_name
        self.lname = l_name
        self.age = age
        self.salary = salary

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def salary(self):
        return self.salary

    def __str__(self):
        return self.fname
    
    def __repr__(self):
        return f"{self.fname} {self.lname} and age is {self.age}"
    
    @staticmethod
    def status():
        return 'status is good'
    
    @classmethod
    def instance_status(cls):
        return f"There are {cls.count_instance} instances of Person class"
    


obj = Person('rahul', 'ahirwar', 34, 54000)
print(f"obj=={obj}")
obj1 = Person('n1', 'm1', 65, 90000)
print(Person.instance_status())

print(repr(obj)) # calling repr method


