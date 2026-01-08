#take input from user

number = input("Enter your number :")
number = int(number)
print(number)

first = number // 10
last = number % 10


print(first) #7
print(last) #5

list =['zero','one','two','three','four','five','six','seven','eight','nine']


print(list[first]," ",list[last])