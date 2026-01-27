# Program count Digits in String

mix_string =input("Enter String : ")
num_list = ['0','1','2','3','4','5','6','7','8','9']
count = 0

for digit in mix_string :
    if digit in num_list :
        count = count + 1
        
print('Total numbers in String : ',count)