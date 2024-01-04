class Single:
    obj = None
    
    def __new__(cls):
        if cls.obj:
            return cls.obj
        else:
            cls.obj = super().__new__(cls)
            return cls.obj
    
    def become_pm(self,name):
        if Single._pm is None:
            Single._pm = name
            print(f"{name} is now our new pm")
        else:
            print(f"cannot become pm!!!!!!!")
            
obj1 = Single()
obj1.awanish = "asdjfl"
obj2 = Single()

print(id(obj1))
print(id(obj2))
print(obj2.awanish)
# print(obj1)
# print(obj2)

