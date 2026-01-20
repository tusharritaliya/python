''' write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days 
'''

month = int(input("Enter Month : "))

if month == 2 :
    print("This Month has 28 or 29 Days")
elif month== 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print("This Month has 31 Days")
elif month == 4 or month == 6 or month == 9 or month == 11 :
    print("This Month has 30 Days")
else :
    print("Invalid Month ")