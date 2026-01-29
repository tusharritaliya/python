
k=0
l=4   
for i in range(5, 0, -1):
    for s in range(0,k):
        print(' ',end='')
    for j in range(i, 0, -1):
        print('*', end=" ")
    print('')
    k=k+1
 
for i in range(0,5):
    for s in range(l,i,-1):
        print(' ',end='')
    for j in range(0,i+1):
        print('*', end=" ")
    print('')
    k=k+1