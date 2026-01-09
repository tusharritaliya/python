#take input from user

number = input("Enter Three Digit Number :")
number = int(number)
print(number)

temp = number // 10 #provide first two digit
last = number % 10 # provide Last
mid = temp % 10 # provide mid
first = temp // 10 #provide first digit

list =['zero','one','two','three','four','five','six','seven','eight','nine']


print(list[first]," ",list[mid]," ",list[last])