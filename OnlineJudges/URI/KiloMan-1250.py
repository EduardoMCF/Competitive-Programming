n = raw_input()
for i in xrange(int(n)):
    n=0
    t,a,s = raw_input(),map(int,raw_input().split()),raw_input()
    for i in xrange(int(t)):
        if s[i]=='J' and a[i]>2: n+=1
        elif s[i]=='S' and a[i]<=2: n+=1
    print n

