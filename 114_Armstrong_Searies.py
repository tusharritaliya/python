n = int(input("Enter the limit: "))

print("Armstrong numbers are:")

for num in range(1, n + 1):
    temp = num
    count = 0
    sum = 0
    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    if sum == num:
        print(num)