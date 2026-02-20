c = float(input("Enter temperature in Celsius: "))

fahrenheit = lambda c: (c * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit(c))