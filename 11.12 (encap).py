#managling
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp = Employee("Jessa ",10000)
print("Name : ",emp.name)
print("Salary : ",emp._Employee__salary)'''

#managling inherit
class Employee:
    def __init__(self,name,salary):
        self.name=name # public
        self.__salary=salary # private

class Manager(Employee):
    def __init__(self,name,salary,Id):
        super().__init__(name,salary)
        self.__Id=Id # private

emp = Manager("Jessa ",10000,123)
print("Name : ",emp.name)
print("Salary : ",emp._Employee__salary)
print("Id : ",emp._Manager__Id)
