def p(x,y):
    for i in xrange(y,x+1):
        c,b=0,1
        if i == 1: b=0
        for j in xrange(2,int(i**(0.5))+1):
            if i%j==0:
                b=0
                break
        if b: print i
n = int(raw_input())
for i in xrange(n):
    y,x = raw_input().split()
    p(int(x),int(y))
    if i!=(n-1): print