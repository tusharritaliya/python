# write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 

hour =int(input("Enter Hours :"))

if hour <=12 :
    print("Time is ",hour,"AM")

if hour >=12 and hour < 25:
    print("Time is ",(hour-12),"PM")

if hour > 24 :
    print("Invalid Input")