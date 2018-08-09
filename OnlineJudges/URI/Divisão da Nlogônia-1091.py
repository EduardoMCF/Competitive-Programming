while True:
    k = raw_input()
    if k == '0': break
    n,m= map(int,raw_input().split())
    for i in range(int(k)):
        x,y = map(int,raw_input().split())
        if x > n and y > m: print 'NE'
        elif x > n and y < m: print 'SE'
        elif x < n and y > m: print 'NO'
        elif x < n and y < m: print 'SO'
        else: print 'divisa'