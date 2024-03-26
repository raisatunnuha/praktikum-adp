for x in range(0,80) :
    x+=1
    if x%4==0 :
        print ('DOR', end = '  ')
        if x % 8 == 0 :
            print(' ')
    else :
        print(x, end = '  ')