# Private_access_modifiers 
class Student: 
    def __init__(self, age, name): 
        self.__age = age
        
        def __funName(self):
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"pythonlobby")
obj1 = Subject

# calling by object reference of class Student
print(obj.__age)
print(obj.__funName())

# calling by object reference of class Subject
print(obj1.__age)
print(obj1.__funName())
