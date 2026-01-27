data = ["Tushar Patel", "Python123", "@All The Best"]


vowels = "aeiouAEIOU"
vowel = 0
consonant = 0
number = 0
word = 0
symbol = 0

in_word = False

text = " ".join(data)   

for ch in text:
    if ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z':
        if not in_word:
            word += 1
            in_word = True

        if ch in vowels:
            vowel += 1
        else:
            consonant += 1

    elif ch >= '0' and ch <= '9':
        number += 1
        in_word = False

    elif ch == ' ':
        in_word = False

    else:
        symbol += 1
        in_word = False

print("Vowels :", vowel)
print("Consonants :", consonant)
print("Numbers :", number)
print("Words :", word)
print("Symbols :", symbol)

