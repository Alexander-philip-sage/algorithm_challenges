import sys
def meta_decorator(arg):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(tup[0], tup[1])) ** power for tup in list_of_tuples]
        return inner
    if callable(arg):
        power = 2
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list


@meta_decorator
def add_together(a, b):
    return a + b


def add(a, b):
    def add_list(a, b):
        ret = []
        for i in range(len(a)):
            ret.append(a[i]+b[i])
        return ret
    if type(a)!= type(b):
        raise TypeError("expecting types to be the same")
    if type(a)==int or type(a)==float:
        return a + b
    elif type(a)== tuple:
        return tuple(add_list(a, b))
    elif type(a) == list:
        return add_list(a, b)
    else:
        raise TypeError("data type not supported yet: " + str(type(a)))

def test_decorators():
    print("adding (2, 3), (3, 4)")
    print(add_together([(2, 3), (3, 4)]))
    try:
        val = add_together(2, 3)
    except TypeError:
        print("this isn't a smart way to handle this since it isn't backwards compatible.... online tutorials aren't always very good")
        print("you can no longer pass in two numbers")
    else: 
        print("adding 2, 3")
        print(val)        
    
    print('\nnow my better add function')
    print("add 2, 3")
    print(add(2,3))
    print("add (2, 3), (3, 4)")
    print(add((2, 3), (3, 4)))
    print("add [2, 3], [3, 4]")
    print(add([2, 3], [3, 4]))
    print("add tom, panda")
    try:
        print(add('tom', 'panda'))
    except TypeError:
        print(sys.exc_info())
    print("add tom, 4")
    try:
        print(add('tom', 4))
    except TypeError:
        print(sys.exc_info())

if __name__=='__main__':

    test_decorators()