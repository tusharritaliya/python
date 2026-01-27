# Count Total words of String

mix_string =input("Enter String : ")

count = 1
for n in mix_string :
    if n == ' ' :
        count = count + 1

print('Total Words is String : ',count)