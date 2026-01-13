# Swap numbers using operator

no1 = int(input("Enter value of A : "))
no2 = int(input("Enter value of B : "))

print(f"Before swap : A = {no1}, B = {no2}") 

tmp = no1 
no1 = no2
no2 = tmp

print(f"After swap : A = {no1}, B = {no2}") 