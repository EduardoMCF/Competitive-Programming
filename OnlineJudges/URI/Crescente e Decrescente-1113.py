while True:
    x,y = raw_input().split()
    x,y = int(x),int(y)
    if x == y:
        break
    if x < y:
        print 'Crescente'
    else:
        print 'Decrescente'