# write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 

print('\n\nAhmedabad To Delhi \n\n')


milege = float(input("Enter your car milege :"))
petrol_price = float(input("Enter Petrol Price/Litr : "))

train_ticket_price = float(input('Input train Ticket Price : '))


print('\nNote : We consider Distance is 986 Km between Ahmedabad to delhi ')

petrol_cost = (986/milege) * petrol_price 

if petrol_cost > train_ticket_price :
    print("\nTrain is Cheaper way ")
else :
    print("\nCar is Cheaper way")