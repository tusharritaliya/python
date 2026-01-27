# Find out odd and even from list using for loop
#count total odd and even number in list

list=[1,2,3,4,5,6,7,8,9,10]
oddCount = 0
evenCount = 0

for number in list :
    if number % 2 == 0 :
        evenCount=evenCount + 1
    else :
        oddCount = oddCount + 1

print('This is the list : ',list)
print('Total odd : ' , oddCount)
print('Total Even : ',evenCount)