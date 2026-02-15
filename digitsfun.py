def digits(text):
    count=0
    for ch in text:
        if ch.isdigit():
            count+=1
    return count
s=input("Enter the string: ")
result=digits(s)
print(result)