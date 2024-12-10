class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployee(self):
        print("Name : ",self.name,"\nAge : ",self.age)

class Manager(Employee):
    def __init__(self,name,age,eid):
        Employee.__init__(self,name,age)
        self.eid=eid
    def displayManager(self):
        print("ID : ",self.eid)

class Developer(Employee):
    def __init__(self,name,age,dept):
        Employee.__init__(self,name,age)
        self.dept=dept
    def displayDeveloper(self):
        print("Department : ",self.dept)

class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamLeader(self):
        self.displayEmployee()
        self.displayManager()
        self.displayDeveloper()
        print("Team Size : ",self.teamsize)

name=input("Enter the Name : ")
age=int(input("Enter the Age : "))
eid=int(input("Enter the Employee Id : "))
dept=input("Enter the Department : ")
teamsize=int(input("Enter the Team Size : "))

person=TeamLeader(name,age,eid,dept,teamsize)
person.displayTeamLeader()



class Student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no 
        self.course=course
    def displayStudent(self):
        print("Name : ",self.name,"\nRoll no : ",self.roll_no,"\nCourse : ",self.course)

class Address(Student):
    def __init__(self,name,roll_no,course,street,area,district):
        Student.__init__(self,name,roll_no,course)
        self.street= street 
        self.area=area
        self.district= district 
    def displayAddress(self):
        print("Street Name : ",self.street,"\nArea : ",self.area,"\nDistrict : ",self.district)

class Contact(Student):
    def __init__(self,name,roll_no,course,ph_no):
        Student.__init__(self,name,roll_no,course)
        self.ph_no=ph_no
    def displayContact(self):
        print("Phone no : ",self.ph_no)
        
class Student_Details(Address,):
    def __init__(self,name,roll_no,course,street,area,district,ph_no,state):
        Student.__init__(self,name,roll_no,course)
        self.street= street 
        self.area=area
        self.district= district
        self.ph_no=ph_no
        self.state= state
    def display_Student_Details(self):
        self.displayStudent()
        self.displayAddress()
        self.displayContact()
        print("State : ",self.state)
        
name=input("Enter the name of the student : ")
roll_no=int(input("Enter the Roll no : "))
course=input("Enter the course :")
street=input("Enter the street name : ")
area=input("Enter the area : ")
district=input("Enter the district : ")
ph_no=int(input("Enter the Phone Number : "))
state=input("Enter the state : ")

Stu=Student_Details(name,roll_no,course,street,area,district,ph_no,state)
Stu.display_Student_Details()





        
