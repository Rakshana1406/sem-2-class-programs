#Question 1
def String(word1,word2):
    merge=[]
    w1=0
    w2=0
    length1=len(word1)
    length2=len(word2)
    while w1<length1 and w2<length2:
        merge.append(word1[w1])
        merge.append(word2[w2])
        w1+=1
        w2+=1
    while w1<length1:
        merge.append(word1[w1])
        w1+=1
    while w2<length2:
        merge.append(word2[w2])
        w2+=1
    print(" ".join(merge))
word1=input("Enter the word 1 : ")
word2=input("Enter the word 2 : ")
String(word1,word2)


#Question 2

def can_place_flowers(flowerbed, n):
    count = 0
    length = len(flowerbed)    
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True    
    return False

print(can_place_flowers([1, 0, 0, 0, 1], 1))  
print(can_place_flowers([1, 0, 0, 0, 1], 2))
                          

        
