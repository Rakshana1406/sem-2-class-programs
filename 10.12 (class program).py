class Student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no 
        self.course=course
    def displayStudent(self):
        print("Name : ",self.name,"\nRoll no : ",self.roll_no,"\nCourse : ",self.course)

class Address:
    def __init__(self,street,area,district):
        self.street= street 
        self.area=area
        self.district= district 
    def displayAddress(self):
        print("Street Name : ",self.street,"\nArea : ",self.area,"\nDistrict : ",self.district)

class Student_Details(Student,Address):
    def __init__(self,name,roll_no,course,street,area,district,state):
        Student.__init__(self,name,roll_no,course)
        Address.__init__(self,street,area,district)
        self.state= state
    def display_Student_Details(self):
        self.displayStudent()
        self.displayAddress()
        print("State : ",self.state)
name=input("Enter the name of the student : ")
roll_no=int(input("Enter the Roll no : "))
course=input("Enter the course :")
street=input("Enter the street name : ")
area=input("Enter the area : ")
district=input("Enter the district : ")
state=input("Enter the state : ")
Stu=Student_Details(name,roll_no,course,street,area,district,state)
Stu.display_Student_Details()
