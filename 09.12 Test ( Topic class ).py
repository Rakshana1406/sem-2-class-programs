class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def displayStudent(self):
        print("Name : ",self.name,"\nRoll no ",self.roll_no)

class Marks(Student):
    def __init__(self,name,roll_no,mark1,mark2,mark3):
        Student.__init__(self,name,roll_no)
        self.mark1= mark1
        self.mark2=mark2
        self.mark3=mark3  
    def displayMarks(self):
        self.displayStudent()
        total=self.mark1+self.mark2+self.mark3
        percent=(total/300)*100
        print("Percentage : ",percent)


Stu=Marks("Rakshana",25,90,89,88)
Stu.displayMarks()
