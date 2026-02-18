l=[1,2,3,4,5]
even=0
odd=0
for n in l:
    if n%2==0:
        even+=1
    else:
        odd+=1
print("The number of even numbers is: ",even)
print("The number of odd numbers is: ",odd)