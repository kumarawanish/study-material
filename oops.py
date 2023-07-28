class Test:
    # operator overloading : basically one operator can perform multiple task like + can add two numbers and cancatenate two str etc...
    
    def overload(self, a, b):
        if isinstance(a, str) and isinstance(b,str):
            return a+b
        elif isinstance(a, int) and isinstance(b,int):
            return a+b
        elif isinstance(a, list) and isinstance(b,list):
            return a+b
        else:
            return "No Operation will be performed..."
        
    # method overloading is not supported by python but we can achieve it by some sample trick.

    def add(self, a=None,b=None,c=None):
        if a and b and c:
            return a+b+c
        elif a and b:
            return a+b
        elif a:
            return a

        
test = Test()

b = test.overload([1,2], [3,4])

c= test.add(10,20)
print(c)




