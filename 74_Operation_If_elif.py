''' write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements. '''

number_1 = float(input("Enter Number 1: "))
number_2 = float(input("Enter Number 2: "))

print('------------------------------------')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

choice = int(input("Enter Choice :"))

if choice == 1 :
    print('Addition : ',(number_1 + number_2))
elif choice == 2 :
    print('Subtraction : ',(number_1 - number_2))
elif choice == 3 :
    print('Multiplication : ',(number_1 * number_2))
elif choice == 4 :
    print('Division : ',(number_1 / number_2))    
else :
    print('Invalid Choice ')