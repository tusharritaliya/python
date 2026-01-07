books = {"book_id": 101, "name": "Python Basics", "author": "Guido van Rossum", "price": 499, "publisher": "Tech Press", "year": 2024}

print(books)
books["Pages"]=198
# books1 = books #bad practice of copy
print(books.get("name")) 

print('Print all items :',books.items())
print('Print keys :',books.keys())
print('Print values :',books.values())

books.pop('Pages')

print('Dictionary after Pop :',books)

books.popitem()

print('Dictionary after delete last pair :',books)


#create new dictionary from list 

Keys =['Name','Age','Gender']

newDict = books.fromkeys(Keys)

print('New Dictionary fromkeys of List ',newDict)
