# write a program to create function that convert given fahrenheit into celsius 
f = float(input("Enter temperature in Fahrenheit: "))

def convertIntoCelsius(cel) :
    c = (f - 32) * 5/9
    return c
    
celsius = convertIntoCelsius(f)

print("Temperature in Celsius:", celsius)