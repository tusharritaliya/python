
# create set

names ={'Rahul','Rohan','manish','Rajesh','Mohit'}

#print Set
print(names)

#add new item
names.add('Jitesh')
print("Set after add ",names)

#update item
names.update(["Yash","Ketan","Tushar"])
print('set after update :',names)

#remove
names.remove('Rahul')
print('Set after remove :',names)

#try to add duplicate item
names.add('Yash')
print('Set after add duplicate record :',names)


a ={1,2,3,4,5}
b ={3,4,5,6,7}

#union
print('Union : ',a.union(b))

#intersaction
print("Intersaction : ",a.intersection(b))

#difference
print("Difference :",a.difference(b))  # a-b