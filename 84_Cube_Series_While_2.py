
print("Program To Print Cube(+,-) series :")
print ('______________________________________')
num = 1
no = int(input("Enter number : "))
while num <= no :
    if pow(num,3) % 2 ==0:
        print(-pow(num,3),end=" ")
    else :
        print(pow(num,3),end=" ")   
    num = num + 1