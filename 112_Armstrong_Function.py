def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        return True
    else:
        return False
        
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")