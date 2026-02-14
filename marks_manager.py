students={}
def add_student():
    name=input("Enter Student name: ")
    marks=int(input("Enter marks: "))
    students[name]=marks
    print("Student added succesfully!\n")

def view_students():
    if not students:
        print("no student record found\n")
        return
    print("\nstudent Records:")
    for name,marks in students.items():
        print(name,"-",marks)
    print()

def average_marks():

    if not students:
        print("no data availabale.\n")
        return
    count=0
    total=0
    for marks in students.values():
        total+=marks
        count+=1
    avg = total/count
    print("average marks: ",avg,"\n")

while True:
    print("=====student marks manager=====")
    print("1.Add student")
    print("2.View students")
    print("3.Average marks")
    print("4.exit")

    choice=input("choose option:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        average_marks()
    elif choice=="4":
        print("program closed.")
        break
    else:
        print("invalid choice\n")
