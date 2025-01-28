""""
#class
class Student:
    s_name="Rakshana"
    s_dept="AI"

s=Student()  #object creation -> objectname=classname()
s.s_name="Rakshana"
s.s_dept="AI"
    
print(f"Name={s.s_name} \n Department={s.s_dept}")
print("\n.................................")

class Student:
    s_name=" "
    s_dept=" "

s=Student()  #object creation -> objectname=classname()
s_name="Rakshana"
s_dept="AI"
    
print(f"Name={s.s_name} \n Department={s.s_dept}")
print("\n.................................")    
    
class Student:
    s_name=" "
    s_dept=" "

s=Student()  #object creation -> objectname=classname()
s.s_name="Rakshana"
s.s_dept="AI"
    
print(f"Name={s.s_name} \n Department={s.s_dept}")
print("\n.................................")

class Student:
    s_name=" "
    s_dept=" "
    
s1=Student() # object 1
s2=Student() # object 2

s1.s_name="Rakshana"
s1.s_dept="AI"

s2.s_name="Makila"
s2.s_dept="AI"
    
print(f"Name={s.s_name} \n Department={s.s_dept}")

print("\nAssign values based on object2")
print("\n.................................")

# class method

class Student:
    name="Rakshana"
    dept="AI"

    def display(self):
        print(f"Name={self.name} \n Deptartent={self.dept}")

s=Student() # Object creation

s.display() # method call
print("\n..................................")

# class with constructor

class Student:
    
    #constructor -- assign values to the class attributes
    def __init__(self ,name=" "):
        self.name=name

    def display(self):
        print("Student details")
        print("Name=",self.name)


s=Student("Rakshana")   # first line of execution
print("Outside the class")
s.display()
print("\n...................................")

class Student:
   
    #constructor -- assign values to the class attributes
    def __init__(self ,name=" "):
        self.name=name

    def display(self):
        print("Student details")
        print("Name=",self.name)

s_name=input()  # first line of execution
s=Student(s_name)
print("Outside the class")
s.display()
print("\n.......................................")
"""

class Student:

    ID=" " #class variable
    #constructor -- assign values to the class attributes
    def __init__(self ,name=" "):
        self.name=name #instant variable
        
    def getData(self):
        self.ID=input("Enter ID : ")
        
    def display(self):
        print("Student details")
        print("Name=",self.name)
        print("ID=",self.ID)

s_name=input("Enter the name : ")  # first line of execution
s=Student(s_name)
s.getData()
s.display()
print("\n.......................................")




















