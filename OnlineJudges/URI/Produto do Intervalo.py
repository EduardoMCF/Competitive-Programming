from sys import stdin,stdout
rr,w = stdin.readline,stdout.write

mp,it = map,int
while True:
    inp = rr().split()
    if not inp: break
    n,k = mp(it,inp)
    arr = mp(it,rr().split())
    arr = [(1 if elem > 0 else -1) if elem else 0 for elem in arr]
    #build
    segtree = [1]*(2*n)
    for i in xrange(n):
        segtree[n+i] = arr[i]

    for i in xrange(n-1,0,-1):
        segtree[i] = segtree[i << 1] * segtree[(i << 1)+1]

    chars = ['0','+','-']
    buffer,c = [0]*k,0
    for _ in xrange(k):
        op,l,r = rr().split()
        l,r = it(l,10)-1,it(r,10)
        if op == 'P':
            # query
            result = 1
            l += n; r += n
            while l < r:
                if l&1:  result *= segtree[l];l+=1
                if r&1:  r-=1; result *= segtree[r]
                l >>= 1; r >>= 1
            buffer[c] = chars[result]
            c+=1
        else:
            #update
            elem = segtree[l+n]
            r = (1 if r > 0 else -1) if r else 0
            if elem != r:
                l += n
                segtree[l] = r
                while l > 1:
                    l >>= 1
                    segtree[l] = segtree[2*l] * segtree[2*l+1]
    w('%s\n' %''.join(buffer[:c]))
