'''write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20 '''
    
    
day = int(input("Enter Birth Day : "))
month = input('Birth Month :')

month = month.lower()


if day < 1 and day > 31 :
    print('Invalid Choice')
    
elif (month == 'march' and day >= 21) or (month == 'april' and day <= 19):
    print('Zodiac Sign : Aries')

elif (month == 'april' and day >= 20) or (month == 'may' and day <= 20):
    print('Zodiac Sign : Taurus')

elif (month == 'may' and day >= 21) or (month == 'june' and day <= 21):
    print('Zodiac Sign : Gemini')

elif (month == 'june' and day >= 22) or (month == 'july' and day <= 22):
    print('Zodiac Sign : Cancer')

elif (month == 'july' and day >= 23) or (month == 'august' and day <= 22):
    print('Zodiac Sign : Leo')

elif (month == 'august' and day >= 23) or (month == 'september' and day <= 22):
    print('Zodiac Sign : Virgo')

elif (month == 'september' and day >= 23) or (month == 'october' and day <= 22):
    print('Zodiac Sign : Libra')

elif (month == 'october' and day >= 23) or (month == 'november' and day <= 21):
    print('Zodiac Sign : Scorpio')

elif (month == 'november' and day >= 22) or (month == 'december' and day <= 21):
    print('Zodiac Sign : Sagittarius')

elif (month == 'december' and day >= 22) or (month == 'january' and day <= 19):
    print('Zodiac Sign : Capricorn')

elif (month == 'january' and day >= 20) or (month == 'february' and day <= 18):
    print('Zodiac Sign : Aquarius')

elif (month == 'february' and day >= 19) or (month == 'march' and day <= 20):
    print('Zodiac Sign : Pisces')

else:
    print("Invalid Date or Month")
