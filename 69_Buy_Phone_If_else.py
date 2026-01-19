# write a program to find out which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india.

us_price = int(input("Enter Iphone price of USA : "))
us_tax = int(input("Enter Sales tax of USA : "))
india_price = int(input("Enter Iphone Price of India :"))

india_custom = 38.5
us_final_price = us_price+(us_price * 8/100)

us_india_price = (us_final_price * 90)
final_indian_price = us_india_price +(us_price*india_custom/100)

print('USA Price : ',final_indian_price)


if final_indian_price > india_price :
    print('Iphone Buy from India is Cheaper with ',(final_indian_price-india_price))
else :
    print('Iphone Buy from USA is Cheaper with ',abs( india_price-final_indian_price))
