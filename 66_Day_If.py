# write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)

day = int(input("Enter Day : "))

if day == 1 :
    print('its Monday')

if day == 2 :
    print('its Tuesday')

if day == 3 :
    print('its Wednesday')

if day == 4 :
    print('its Thursday')

if day == 5 :
    print('its Friday')

if day == 6 :
    print('its Saturday')

if day == 7 :
    print('its Sunday')

if day <=0 or day >=8 :
    print("Invalid Input")