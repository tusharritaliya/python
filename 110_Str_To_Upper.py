def to_upper(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result
str =input('Entet String :')

print(to_upper(str)) 