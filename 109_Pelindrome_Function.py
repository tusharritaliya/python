def is_palindrome(text):
    return text == text[::-1]

str = input('Enter String:')
print(is_palindrome(str) )