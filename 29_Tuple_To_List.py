#Given a tuple of numbers, convert it into a list and add new elements.

tup = (1,2,3,4,5,6,7,8,9,10)

print("Tuple ",tup)

my_list = list(tup)

print("List is ",my_list)

my_list.append(11)
my_list.append(12)

print("List after insert :",my_list)