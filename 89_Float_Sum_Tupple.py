# Find out sub of Float number of tupple

tup =(12.2,12,23.32,45.02,23,56,212.2,99.78,45.10,23)
sum = 0
count = 0
for number in tup :
    if isinstance(number,float) :
        sum = sum + number
        count = count + 1

avg = sum/count

print('Sum of Float number is : ',sum)
print('Average of Float number is : ',avg)