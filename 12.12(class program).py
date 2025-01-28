import random
class Customer:
    def __init__(self,cust_id,name,phone):
        self.cust_id=cust_id
        self.name=name
        self.phone=phone

    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"

    def verify_customer_id(cust_id):
        if cust_id[0:4]=="TICK" and cust_id[4:8].isdigit():
            print("Valid")
        else:
            print("Invalid")


print("**********************Welcome To Ticket Booking Program***************************")
cust_id=input("Enter the Customer Id : ")
Customer.verify_customer_id(cust_id)
