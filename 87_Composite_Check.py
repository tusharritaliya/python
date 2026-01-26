# Check number is Composite or not 

num = int(input("Enter Number : "))

factors = 0
i = 1 

while i <= num :
    if num % i == 0 :
        factors = factors + 1
    i =  i + 1
if factors >=3 :
    print("Number is Composite")
else :
    print("Number not is Composite")