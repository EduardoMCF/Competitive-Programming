while True:
    p,s = raw_input().split()
    if p+s == '00': break
    p = int(p)
    t1,t2,t3 = raw_input().split()
    t1,t2,t3=int(t1),int(t2),int(t3)
    q,j,c=[0,0,0,0,0,0,0,0,0,0],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],0
    n = raw_input()
    for i in xrange(int(n)):
        x,y = raw_input().split()
        x,y = int(x),int(y)
        while True:
            j[c] *= -1
            if j[c] == 1:
                q[c] += x+y
                if q[c]!= t1 and q[c] != t2 and q[c] != t3: j[c] *= -1
                break
            else:
                c+=1
                if c == p: c=0
        c+=1
        if c == p:c=0
    print q.index(max(q)) + 1

