def reverse_string(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    return rev
str=input("Enter String:")
print(reverse_string(str) )