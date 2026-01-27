# Nagative to Positive
numbers = [10, -5, 20, -15, 0, 8, -3]
print('List Before Conversion :',numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = -numbers[i]
 
        
print('List After Conversion :',numbers)
