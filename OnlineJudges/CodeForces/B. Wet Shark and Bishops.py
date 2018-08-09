import collections
t=int(raw_input())
s,da,ds=0,collections.defaultdict(int),collections.defaultdict(int)
for i in xrange(t):
    x,y=map(int,raw_input().split())
    t1,t2=x-y+1000,x+y
    ds[t1] += 1
    da[t2] += 1
for i in xrange(2001):
    s += ds[i]*(ds[i]-1)/2
    s += da[i]*(da[i]-1)/2
print s

