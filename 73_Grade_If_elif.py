'''  Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------

'''
subject1 = int(input("Enter Marks of Subject 1 : "))
subject2 = int(input("Enter Marks of Subject 2 : "))
subject3 = int(input("Enter Marks of Subject 3 : "))
subject4 = int(input("Enter Marks of Subject 4 : "))
subject5 = int(input("Enter Marks of Subject 5 : "))

total = subject1 + subject2 + subject3 + subject4 + subject5 

per = total /5
grade = None

if per >= 90 :
    grade =" A+"
elif per >= 80 :
    grade=" A"
elif per >= 70 :
    grade=" B"
elif per >= 60 :
    grade=" C"
elif per >= 50 :
    grade=" D"
else :
    grade = " Needs Improvement"
    
print(f"Total : {total}\nPercentage : {per}\nGrade : {grade}")