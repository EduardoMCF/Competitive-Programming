from sys import stdin,stdout
from collections import defaultdict
from bisect import bisect_right
r,w = stdin.readline,stdout.write

n = int(r(),10)
arr = map(int,r().split())
resps,ans,MIN,ABS,MAX,STR = defaultdict(int),[0]*(n+1),min,abs,max,str

# Log preprocess
log = [0] * (n+1)
for i in xrange(2,n+1): log[i] = log[i//2] + 1

# Shift preprocess
pow = [1 << i for i in xrange(log[n]+1)]

# build sparse table
k = log[n]+1
sTable = [[0]*k for i in xrange(n+1)]

for i in xrange(n):
    sTable[i][0] = arr[i]

for j in xrange(1,k+1):
    for i in xrange(n+1):
        if i + (1 << j) > n: break
        sTable[i][j] = MIN(sTable[i][j-1], sTable[i + pow[j-1]][j-1])

for i in xrange(n):
    elem = arr[i]
    l,r,res = 0,i-1,0
    while l <= r:
        m = (l+r) >> 1; j = log[i-m+1]
        # m:i
        if elem == MIN(sTable[m][j], sTable[i-pow[j]+1][j]): r = m - 1;res = ABS(m-i)
        else: l = m + 1

    l,r,res1 = i+1,n-1,0
    while l <= r:
        m = (l+r) >> 1; j = log[m-i+1]
        # i:m
        if elem == MIN(sTable[i][j], sTable[m-pow[j]+1][j]): l = m + 1; res1 = ABS(m-i)
        else: r = m - 1

    resps[res+res1+1] = MAX(resps[res+res1+1],elem)

# counting sort
counter = [0] * (max(resps)+1)
for i in resps:
    counter[i] += 1

ndx = 0
sortedResps = [0] * len(resps)
for i in range(len(counter)-1,-1,-1):
    while counter[i]:
        sortedResps[ndx] = (i,resps[i])
        ndx += 1
        counter[i] -= 1


#solve
maxx,j = -1,0
for i in xrange(n,0,-1):
    while j < len(sortedResps):
        if sortedResps[j][0] >= i: maxx = MAX(maxx,sortedResps[j][1]); j+=1
        else: break
    ans[i] = maxx


w(' '.join(map(STR,ans[1:])))
