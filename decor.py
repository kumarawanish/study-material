
def outer(*args, **dkwargs):
    """This decorator takes an argument like dtype"""

    def decor(add):
        def inner(*args,**kwargs):
            dtype = dkwargs.get('dtype')

            output = None

            if dtype == int:
                output = 1

                for arg in args:
                    output *= arg

                return output
            
            elif dtype == 'str':
                return 'Not Implemented Yet.'

        return inner
    return decor


@outer(dtype=str)
def add(a,b):
    """This is add function"""

    c = a+b
    return c

print(add(2,7))
# print(help(add))
