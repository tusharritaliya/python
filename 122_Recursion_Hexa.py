def to_hex(n):
    digits = "0123456789ABCDEF"
    if n < 16:
        return digits[n]
    return to_hex(n // 16) + digits[n % 16]

num = int(input("Enter a decimal number: "))
if num == 0:
    print("Hexadecimal: 0")
else:
    print("Hexadecimal:", to_hex(num))
