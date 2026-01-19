# write a program to find out whether given year is millennium year or not. using if else decision making statements.

year = int(input("Enter Year : "))

if year % 1000 == 0 :
    print('Year is Millennium')
else :
    print('Year is not Millennium')