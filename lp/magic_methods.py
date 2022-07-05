class User:

    username = 'root'

    def __new__(cls, salary): # creates an object (instance of the class) ...
        print('... New instance created ...')
        obj = object.__new__(cls)
        return obj

    def __init__(self, salary) -> None: # initializes arguments
        print('... Arguments initialized ...')
        self.salary = salary

    def __add__(self, obj): # initially is used to add nums, though can be overridden ... 
        return self.salary + obj.salary

    def get_username(cls): # cls refers to the class (a class method) ...
        return cls.username # -> class variable

    def get_salary(self): # self refers to the instance (an instance method) ...
        return self.salary # -> instance variable

    def __str__(self) -> str:
        return f'{self.salary} | {self.username}' # returns a printable string representation of class ...  

    def __del__(self): # called when object gets destructed and all its references are to be eliminated ...
        print('... Destructor called ...')

class Admin(User):

    def __add__(self, obj):
        return self.salary + obj.salary

uname = User(1000)
print(uname)
del uname # <del> used to delete objects (including: instances of a class, lists, tuples, dictionaries, etc)