# write a program to find out whether given year is leap year or not

year = int(input("Enter year")) # 2026
if year < 1:
    print("invalid year")
else:
    rmd1 = year % 4 #2
    rmd2 = year % 100 # 26
    rmd3 = year % 400 # 26
    if rmd1==0 and rmd2!=0:
        print("Given year is leap year")
    else:
        if rmd2==0 and rmd3==0:
            print("Given year is leap year")
        else:
            print("Given year is not leap year")