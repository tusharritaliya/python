def count_spaces(text):
    count = 0
    for ch in text:
        if ch == ' ':
            count += 1
    return count
str =input('Enter String :')
print(count_spaces(str)) 