while True:
    x1,y1,x,y = raw_input().split()
    if x1+y1+x+y == '0000': break
    if (x1,y1) == (x,y): print '0'
    elif (x1 == x and y1 != y) or (y1 == y and x1 != x) or abs(int(x1) - int(x)) == abs(int(y1) - int(y)):print '1'
    else: print '2'

