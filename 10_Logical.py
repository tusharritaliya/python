# Logical Operator 

num1 =int(input("Enter value of num1 :"))
num2 =int(input("Enter value of num2 :"))
num3 =int(input("Enter value of num3 :"))

ans = num1 > num2 and num2 >= num3 
print(f"{ans}={num1} > {num2} and {num2} >= {num3} ")  

ans = num1 > num2 or num2 <= num3 
print(f"{ans}={num1} > {num2} or {num2} <= {num3} ")  

ans = not(num1 >= num2 and  num2 < num3) 
print(f"{ans}={num1} >= {num2} and {num2} < {num3} ")  