# Currency

rupee = int(input("Enter Money :"))
bud = rupee
#For 500 note
_Note500 = bud // 500 
print(f"500 X {_Note500} = {_Note500 * 500}")
bud = bud - (_Note500 * 500) 

#For 200 note
_Note200 = bud //200  
print(f"200 X {_Note200} = {_Note200 * 200}")
bud = bud - (_Note200 * 200 ) 

#For 100 note
_Note100 = bud // 100
print(f"100 X {_Note100} = {_Note100 * 100}")
bud = bud - (_Note100 * 100 ) 

#For 50 note
_Note50 = bud // 50

print(f"50 X {_Note50} = {_Note50 * 50}")
bud = bud - (_Note50 * 50 ) 

#For 20 Note
_Note20 = bud // 20
print(f"20 X {_Note20} = {_Note20 * 20}")
bud = bud - (_Note20 * 20 ) 

#For 10 Note
_Note10 = bud // 10
print(f"10 X {_Note10} = {_Note10 * 10}")
bud = bud - (_Note10 * 10) 

#For 5₹ coin
_Note5 = bud // 5
print(f"5 X {_Note5} = {_Note5 * 5}")
bud = bud - (_Note5 * 5 ) 

#for 2₹ coin
_Note2 = bud // 2
print(f"2 X {_Note2} = {_Note2 * 2}")
bud = bud - (_Note2 * 2 )

#for 1₹ coin
_Note1 = bud // 1
print(f"1 X {_Note1} = {_Note1 * 1}")