# destructor
class Student:
    def __init__(self,dept,age=18,name="Rakshana"):
        self.age=age
        self.name=name
        self.dept=dept

    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}\nAge={self.age}")
    def __del__(self): # destructor method
        print("Object is destroyed")
stu=Student("AI") # object creation
stu.display()
del stu
         
