def reverse(text):
    rev=""
    for i in range(len(text)-1,-1,-1):
        rev=rev+text[i]
    return rev
s=input("Enter the string: ")
result=reverse(s)
print(result)
        
    