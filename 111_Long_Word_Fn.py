str =input('Enter String :')

def longest_word(text):
    words = text.split()
    return max(words, key=len)
print(longest_word(str)) 