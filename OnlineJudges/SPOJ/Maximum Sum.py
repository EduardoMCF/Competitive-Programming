from sys import stdin,stdout
rr,w = stdin.readline,stdout.write

def build():
    segtree = [[0,0] for _ in xrange(2*n)]
    mx,mn = max,min

    for i in xrange(n):
        segtree[n+i][0] = arr[i]

    for i in xrange(n-1,0,-1):
        g1,g2 = segtree[pow[i]],segtree[pow[i]+1]
        max1,max2,smax1,smax2 = g1[0],g2[0],g1[1],g2[1]
        segtree[i] = [mx(max1,max2),mx(smax1,smax2,mn(max1,max2))]

    return segtree

def update(pos, val):
    pos += n
    mx,mn = max,min
    segtree[pos] = [mx(val,segtree[pos][0]),0]

    while pos > 1:
        pos >>= 1
        g1,g2 = segtree[pow[pos]],segtree[pow[pos]+1]
        max1,max2,smax1,smax2 = g1[0],g2[0],g1[1],g2[1]
        segtree[pos] = [mx(max1,max2),mx(smax1,smax2,mn(max1,max2))]

def query(l,r):
    mx,mn = max,min
    result = [0,0];l += n; r += n
    while l < r:
        if l&1:
            g1,g2 = segtree[l],result
            max1,max2,smax1,smax2 = g1[0],g2[0],g1[1],g2[1]
            result = [mx(max1,max2),mx(smax1,smax2,mn(max1,max2))]
            l+=1
        if r&1:
            r-=1;
            g1,g2 = segtree[l],result
            max1,max2,smax1,smax2 = g1[0],g2[0],g1[1],g2[1]
            result = [mx(max1,max2),mx(smax1,smax2,mn(max1,max2))]
        l = rpow[l];r = rpow[r]
    return result[0]+result[1]

it,st,mp = int,str,map
n = it(rr(),10)
pow = [i << 1  for i in xrange(2*n+1)]
rpow = [i >> 1 for i in xrange(2*n+1)]
arr = map(it,rr().split())
t = it(rr(),10)
segtree = build()
for i in xrange(t):
    li = rr().split()
    c = li[0]
    l,r = mp(it,li[1:])
    if c is 'Q': w('%i\n' %query(l-1,r))
    else: update(l-1,r)
