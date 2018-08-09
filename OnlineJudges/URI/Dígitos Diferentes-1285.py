while True:
    try:
        n,m = raw_input().split()
        c=0
        for i in xrange(int(n),int(m)+1):
            if len(set(str(i))) == len(str(i)): c+=1
        print c
    except:
        break