purchase_price = float(input("Enter Purchase Price: "))
selling_price = float(input("Enter Selling Price: "))

difference = selling_price - purchase_price

if difference > 0:
    print("Profit")
    print("Profit Amount:", difference)

elif difference < 0:
    print("Loss")
    print("Loss Amount:", abs(difference))

else:
    print("No Profit No Loss")