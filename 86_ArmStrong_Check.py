# Check number is ArmStrong or not 

num = int(input("Enter Number : "))

num_print = num
sum = 0

while num > 0 :
    reminder = num % 10
    sum = sum + pow(reminder,3)
    num = num // 10

if sum == num_print :
    print("Number is Armstrong")
else :
    print("Number not is Armstrong")