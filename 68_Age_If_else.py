# write a program to find out elder brother from given two brother's age.

person1_age = int(input('Enter Age of Person 1 : '))
person2_age = int(input('Enter Age of Person 2 : '))


if person1_age > person2_age :
    print('Person 1 is elder','Age Diffrence is ',(person1_age - person2_age))
else :
    if person2_age > person1_age :
        print('Person 2 is elder','Age Diffrence is ',(person2_age - person1_age))
    else :
        print('Both age is same')    

    
    
