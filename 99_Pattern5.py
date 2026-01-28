isOne=True
for i in range(1, 6):
    for j in range(1, i + 1):
        if isOne :
            print('1',end=' ')
            isOne = False
        else :
            print('0',end=' ')    
            isOne = True
    print('')