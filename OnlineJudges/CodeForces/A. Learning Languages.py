from collections import defaultdict
n,m = map(int,raw_input())
funci=defaultdict(set)
for i in xrange(n):
    l = map(int,raw_input().split())
    for j in xrange(1,l[0]+1):
        funci[i].add(l[j])
for k in xrange(1,n):
    if funci[k].intersection(funci[k-1]):
        funci[k] = funci[k]+funci[k-1]
