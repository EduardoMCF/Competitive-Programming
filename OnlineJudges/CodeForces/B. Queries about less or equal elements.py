import bisect
n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
a.sort()
for i in xrange(k):
    e = bisect.bisect(a,b[i])
    if i == k-1:print e
    else:print e,

