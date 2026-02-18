numbers=[1,2,3,4,5,5,6,7,8,8,9]
unique=[]
for n in numbers:
    if n  not in  unique:
        unique.append(n)
print(unique)