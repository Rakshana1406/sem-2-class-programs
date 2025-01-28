# unparameterised constructor
class Library:
    def __init__(self): 
        self.bookname="The God of Things"
        self.authorname="Arundhati Roy"
        
    def getBookDetails(self): 
        print(f"Book Name={self.bookname}\nAuthor Name={self.authorname}")

lib=Library()

lib.getBookDetails()

# parameterised constructor
class Student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept

    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")

stu=Student("Rakshana","AI")
stu.display()

# parameterised constructor with default
class Student:
    def __init__(self,dept,age=18,name="Rakshana"):
        self.name=name
        self.dept=dept
        self.age=age

    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}\nAge={self.age}")

stu=Student("AI")
stu.display()

