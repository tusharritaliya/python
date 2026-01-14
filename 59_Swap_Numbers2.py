# Swap numbers without using third variable 

no1 = int(input("Enter value of No1 : "))
no2 = int(input("Enter value of No2 : "))

print (f"Number before swap A = {no1} B = {no2}")
no1 = no1 + no2
no2 = no1 - no2
no1 = no1 - no2

print (f"Number After swap A = {no1} B = {no2}")