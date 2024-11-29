class Employee:
    def __init__(self,name,ID,position):
        self.name=name
        self.ID=ID
        self.position=position
    def displayEmployee(self):
        print("Name : ",self.name,"\nID : ",self.ID,"\nPosition : ",self.position)

class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print("Street : ",self.street,"\nState : ",self.state,"\nCountry : ",self.country)

class EmployeeDetails(Employee,Address):
    def __init__(self,name,ID,position,street,state,country):
        super().__init__(name,ID,position)  # super() --> for the immediate parent or to intialize this variables
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployee()
        self.displayAddressInfo()

ed=EmployeeDetails("Jaya",100,"Manager","Shenoy Nagar","Tamil Nadu","India")
ed.displayEmp()














        
        
        
