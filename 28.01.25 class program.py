#Question 1

num=int(input("Enter the number : "))
arr=[]
for i in range(num):
    x=input("Enter the element : ")
    arr.append(x)
print("Array : ",arr)
print("The output of the array is")
for i,j in enumerate(arr):
    print(j,"- index of array is  ",[i])

#Question 2

num=int(input("Enter the number : "))
arr=[]
for i in range(num):
    x=input("Enter the element : ")
    arr.append(x)
print("Array : ",arr)
x=int(input("Select the element position to remove - "))
print("The output of array after removing the element is ")
del arr[x]
print(arr)

#Question 3

num=int(input("Enter the number : "))
arr=[]
for i in range(num):
    x=input("Enter the element : ")
    arr.append(x)
print("Array : ",arr)
x=int(input("Select the element location to add - "))
y=input("Element to be added : ")
print("The output of array after adding the element is ")
arr.insert(x,y)
print("The array is - "arr)

#Question 4

num=int(input("Enter the number : "))
arr=[]
for i in range(num):
    x=input("Enter the element : ")
    arr.append(x)
print("Array : ",arr)
print("The output of the array is")
for i,j in enumerate(arr):
    print(j,"- index of array is  ",[i])
even=[]
odd=[]
for i,j in enumerate(arr):
    if i%2==0:
        even.append(f"{j} - index of array is {[i]}")
    else:
        odd.append(f"{j} - index of array is {[i]}")
print("Even position elements are ")
for i in even:
    print(i)               
print("Odd position elements are ")
for i in odd:
    print(i)                
   

    
