#Given two lists, convert them into sets and find common elements.

list1 =[1,2,3,4,5,5]
list2 =[2,3,4,5,6,6]


set1 = set(list1)
set2 = set(list2)

print("set 1 :",set1)
print("Set 2 :",set2)


print("Comman elements :",set1.intersection(set2))