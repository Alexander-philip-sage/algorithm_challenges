from private_protected import test_private
from decorators import test_decorators


def check_memory_addr(a, b):
    if (id(a)==id(b)):
        print("Python caches some integers , so integers in that range are usually but not always identical."
            "What you see for 257 is the Python compiler optimizing identical literals when compiled in the same code object."
            "the Python bytecode compiler is not able to perform massive optimizations (like statically typed languages), "
            "but it does more than you think. One of these things is to analyze usage of literals and avoid duplicating them."
            "Note that this does not have to do with the cache, because it works also for floats, which do not have a cache")
        print("input", a)
        print("a", id(a))
        print("b", id(b))
    else:
        print("a and b have the same value but the object addresses don't point to the same instance. like in C")

def variable_name_rules():
    print("variables are case sensitive")
    var = 4
    print("var")
    print(var)
    Var = 6
    print("Var")
    print(Var)
    print("var")
    print(var)
    print("you can override a built in type as a variable name which would be a terrible idea")
    str = 4
    print("str")
    print(str)

       # pass = 4
     #   print(pass)

    print("thankfully you cannot override a keyword")

def test_memory_address():
    with open("test.txt", 'r+') as fileobj:
        print(fileobj.read())

    check_memory_addr(257, 257)
    check_memory_addr(10**10, 10**10)
    a = (2, 3) 
    b= (2, 3)
    check_memory_addr(a, b)
    b = (5, 2)

class MyFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

if __name__=="__main__":
    test_private()

    print()
    lst = ['p', 'j', 'c']
    lst.insert(len(lst), 's')
    print(lst)
    print()

    a = 123
    print(type(a))
    print()

    test_decorators()
    print()
    with MyFile("test.txt", 'r') as  fileobj:
        print(fileobj.read())