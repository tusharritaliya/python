# check number is perfect or not

num = int(input("Enter number :"))
sum = 0

i = 1

while i< num :
    if num % i == 0 :
        sum = sum + i
    i=i+1

if sum == num :
    print(f"Number {num} is Perfect number")
else :
    print(f"Number {num} is Not Perfect number")