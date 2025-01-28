import re

def verify_password(password):
    pa=r'^(?=.+1[a-z])(?=.*3[A-Z])(?!.*[0-9])(?!.+[!@#$%^&*()_+=]){12})$'
    if re.match(pa,password):
        print("Password is strong")
    else:
        print("Password is not strong")

password =input("Enter the password : ")
verify_password(password)
