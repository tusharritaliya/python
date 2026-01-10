# Create a list of numbers and remove all duplicate values without using loops.

my_list =[1,1,1,2,2,3,3,4,5,6,7,8,9,10]

print('List with duplicate values ',my_list)
tmp_set = set(my_list)

my_list = list(tmp_set)

print("List after remove duplicate values ",my_list)