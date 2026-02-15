def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_perfect(number):
    print(number, "is a Perfect Number")
else:
    print(number, "is not a Perfect Number")