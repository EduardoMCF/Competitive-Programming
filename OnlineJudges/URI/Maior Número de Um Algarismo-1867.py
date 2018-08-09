while True:
    x,y=raw_input().split()
    if x+y=='00': break
    if (x!='0' and int(x)%10==0) and (y!='0' and int(y)%10==0): x,y=x.strip('0'),y.strip('0')
    x,y=int(x),int(y)
    while x>9: x=sum([int(i) for i in str(x)])
    while y>9: y=sum([int(i) for i in str(y)])
    if x>y: print 1
    elif y>x: print 2
    else: print 0