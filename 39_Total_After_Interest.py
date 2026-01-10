# Write a program to calculate total amount after simple interest.

principle = int(input("Enter Principle amount :"))
rate = int(input("Enter interest rate :"))
n = int(input("Enter Time in year :"))


simple_interest = (principle * rate * n)/100

print(f'Simple interest is {simple_interest+principle}')