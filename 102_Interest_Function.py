# write a program to create function that calculate and return simple interest of given amount rate and year
p=float(input('Enter Amount : '))
r=float(input('Enter Rate : '))
n=float(input('Enter Year : '))

def getInterest(p,r,n) :
    i = p*r*n/100
    return i


interest = getInterest(p,r,n)

print('Interest is ',interest)