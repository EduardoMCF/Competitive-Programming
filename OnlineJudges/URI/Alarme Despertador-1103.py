while True:
    h1,m1,h,m = raw_input().split()
    if h1+m1+h+m == '0000': break
    elif h1+m1 == h+m: print 1440
    else:
        ht = int(h) - int(h1)
        if ht < 0: ht = 24 - (int(h1) - int(h))
        mt = int(m) - int(m1)
        if mt < 0:
            mt = 60 - (int(m1) - int(m))
            ht -= 1
            if ht == -1: ht = 23
        print ht*60 + mt
