#example program
'''class Student:
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
s=Student("Ria")
s.display()


#
class Student:
    id=123
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
s=Student("Ria")
s.display()
print(s.id)

#private
class Student:
    __id=123
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
s=Student("Ria")
s.display()
print(s.id)


class Student:
    __id=123
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
name=input("Enter the name : ")        
s=Student(name)
s.display()
print(s.id)


class Student:
    id=int(input("Enter the id : "))
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
name=input("Enter the name : ")            
s=Student(name)
s.display()
print(s.id)


class Student:
    id=int(input("Enter the id : "))
    dept=input("Enter the department : ")
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
name=input("Enter the name : ")            
s=Student(name)
s.display()
print(s.id)
print(s.dept)


class Student:
    __id=int(input("Enter the id : "))
    __dept=input("Enter the department : ")
    def __init__(self,name):
        self.__name=name
    def display(self): 
        print("Name =",self.__name)
name=input("Enter the name : ")            
s=Student(name)
s.display()
print(s.id)
print(s.dept)
'''

#man
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp = Employee("Jessa ",10000)
print("Name : ",emp.name)
print("Salary : ",emp._Employee__salary)














