from bisect import bisect
a,b = map(int,raw_input().split())
n = a-b
ans = []
if a<b:
    print 0
elif a==b: print "infinity"
else:
    for i in xrange(1,int(n**.5)+1):
        if not n%i: ans.extend([i] if i**2 == n else [i,n/i])
    ans.sort()
    print(len(ans)-bisect(ans,b))
