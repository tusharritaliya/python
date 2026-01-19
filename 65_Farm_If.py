#  write a program to accept length and width of two different farm from user. and find out & display which farm is bigger

print('Enter data of farm 1 :')
print('----------------------')

length1 = float(input("Enter Length of farm 1 : "))
width1 = float(input("Enter Width of farm 1 : "))

print('Enter data of farm 1 :')
print('----------------------')

length2 = float(input("Enter Length of farm 2 : "))
width2 = float(input("Enter Width of farm 2 : "))

area1 = length1 * width1
area2 = length2 * width2


if area1 > area2 :
    print('Farm 1 is Bigger ,Area is ',area1)
if area2 > area1 :
    print('Farm 2 is Bigger,Area is ',area2)
if area1 == area2 :
    print('Both are equal')