class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name : ",self.name,"\nAge : ",self.age)

class Employee(Person):
    def __init__(self,name,age,Id):
        Person.__init__(self,name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("ID : ",self.Id)

class Salary(Person):
    def __init__(self,name,age,salary):
        Person.__init__(self,name,age)
        self.salary=salary
    def displaySalary(self):
        self.displayPerson()
        print("Salary : ",self.salary)

class BankAccounts(Employee,Salary):
    def __init__(self,name,age,Id,salary,Account_no):
        Employee.__init__(self,name,age,Id)
        Salary.__init__(self,name,age,salary)
        self.Account_no=Account_no
    def displayBankDetails(self):
        print("Employee class : ")
        self.displayEmployee()
        print("Salary class : ")
        self.displaySalary()
        print("Account No : ",self.Account_no)

emp=BankAccounts("Ragu",35,3412,25000,9824563849)
emp.displayBankDetails()
        
        

