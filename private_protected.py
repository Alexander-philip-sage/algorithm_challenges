
class Student:
        
    def __init__(self,name: str):
        self.check_name(name)
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,newname: str):
        self.check_name(newname)
        self._name = newname
    def check_name(self, name: str):
        if type(name)!=str:
            raise TypeError("name must be str. you gave " + str(type(name)))
        if len(name) > 150:
            raise Exception("your name is too long")
class Computer:

    primary = "Operating system"
    _C_protected = "protected member c"
    __C_private__ = "private static c"
    @staticmethod
    def purpose():
        print("this class prints general info about OS")

    def __init__(self, oper: str):
        self.oper = oper
        self.__C_private_instance__ = "private instance c"
        self._protected_instance = "protected instance c"
        if self.oper=='unix':
            print("compatible with linux and mac")
        elif self.oper=='windows':
            print("win: most commonly used os")
        elif self.oper=="mobile":
            print("insufficient detail")

    def use_case(self):
        if self.oper=='unix':
            print("good for servers and deployment")
        elif self.oper=='windows':
            print("good for desktop applications which are going out of style")
        elif self.oper=="mobile":
            print("trendy, good for games and sometimes helps people")

    def print_private():
        print("Computers static private variable", Computer.__C_private__, " - accessed from static method")
        print("worked without static method decorator")

    def __str__(self) -> str:
        return self.oper

class Languages(Computer):
    primary = "Language"
    def __init__(self, oper: str, lang: str):
        super().__init__(oper)
        self.lang = lang
        self.__L_private_instance__ = "private instance L"
        if lang =='python':
            self.style = 'interpreted'
            print("needs to be run with a python interpreter on every machine to run - unless using Buck/Bazzel")
        elif lang =='C++':
            self.style = 'compiled'
            print("once compiled on an OS, the machine code can be ported over to other machines with similar OS category")
        elif lang =="Java":
            self.style = 'JIT: javac & JVM'
            print("relies on the JVM to run so as long as the computer has a JVM and it can run the bytecode")

    def get_style(self) -> str:
        return self.style
    def __str__(self) -> str:
        return Computer.primary + ": \t" + super().__str__() + "\n"+Languages.primary+": \t\t" + self.lang + "\nCompiling style: \t" + self.style
    def print_lang_private(self):
        print("private instance variable - accessed within object")
        print(self.__L_private_instance__)
    def print_super_protected(self):
        print("inhereted protected member - accessed within object")
        print(self._protected_instance)
    def print_super_private(self):
        try:
            print(self.__C_private_instance__)
            print("Failed: accessed inhereted private member (subclass)")
        except:
            print("Success: could not access inhereted private variable")

def test_private():
    print("***   ***")
    print("*** Testing inheritance and private/protected restrictions in python***")
    print("***\t\t hint: they're just convention. everything is public***")
    print("***   ***")
    lang = Languages("unix", "python")
    print(lang)
    print()
    print("What is the purpose of Computer class")
    Computer.purpose()
    print()
    try:
        print(Computer.__C_private__)
        print("Failed: global access to private static variable")
    except:
        print("Success: could not access private static variable")
    print()
    Computer.print_private()
    print()
    try:
        print(lang.__L_private_instance__)
        print("Failed: global access to private member variable")
    except:
        print("Success: could not access private instance variable")
    print()
    lang.print_lang_private()
    print()
    lang.print_super_protected()
    print()
    lang.print_super_private()
    print()
    try:
        print(lang.__C_private_instance__)
        print("Failed: global access to inherented private variable")
    except:
        print("Success: could not access inherented private variable")
    print()
    print()
    student = Student("sage")
    try:
        print(student._name)
        print("Failed: global access protected variable"
        " this approach is supposed to make the variable protected")
    except:
        print("Success! could not access protected variable")
    print()
    print("this approach still has some value in that you can "
    "perform checks on the variable being assigned to the name so that the user doesn't make a mistake")
    student._name = 'max'
    print()
    if student._name!= 'sage':
        print("Failed: changed protected member variable with global access")
    print("\ninitializing student name with int")
    try:
        stud = Student(4)
    except Exception as e:
        print(e)
    print("\nsetting the name to an int")
    try:
        student.name = 4
    except Exception as e:
        print(e)
    print("\nsetting the name to a paragraph")
    try:
        student.name = str(list(range(400)))
    except Exception as e:
        print(e)
    print("***   ***")
    print("***Done testing***")
    print("***   ***")
