m=input("Enter the string: ")
rev=""
for i in range(len(m)-1,-1,-1):
    rev=rev+m[i]
print("the reversed string is:",rev)