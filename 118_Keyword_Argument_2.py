def student(name, age, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

n = input("Enter Name: ")
a = int(input("Enter Age: "))
c = input("Enter Course: ")

student(name=n, age=a, course=c)