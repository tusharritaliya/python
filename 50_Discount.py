# Write a program to calculate discount amount using price and discount rate.

price = int(input("Enter price of product :"))
rate = int(input("Discount Rate :"))

discount_price = price - (price * rate)/100

print("Price after Discount : ",discount_price)