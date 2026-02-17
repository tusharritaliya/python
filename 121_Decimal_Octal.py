num = int(input("Enter a decimal number: "))
octal = ""

if num == 0:
    octal = "0"
else:
    while num > 0:
        octal = str(num % 8) + octal
        num = num // 8

print("Octal:", octal)