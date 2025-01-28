'''num=int(input("Enter the number:"))
sum_num=0
while num!=0:
    last=num%10
    sum_num+=(last**3)
    num//=10
print(sum_num)    
'''

string=input()
word=string.split()
length=len(word)
print("Number of words : ",length)
