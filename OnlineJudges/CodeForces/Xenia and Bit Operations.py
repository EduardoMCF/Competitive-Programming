def main():
    from sys import stdin,stdout
    r,w = stdin.readline,stdout.write
    def build():
        segtree,aux = [arr],0
        while True:
            nvl = segtree[-1]
            l = ln(nvl)
            if l <= 1: break
            segtree.append([nvl[_] | nvl[_+1] for _ in xrange(0,l,2)] if not aux else [nvl[_] ^ nvl[_+1] for _ in xrange(0,l,2)])
            aux = not aux
        return segtree

    it,mp,st,ln = int,map,str,len
    n,m = mp(it,stdin.next().rsplit())
    arr = mp(it,stdin.next().rsplit())
    n = 2**n
    segtree = build()
    l = ln(segtree)
    ans=[0]*m
    for j,line in enumerate(stdin):
        pos,val = mp(it,line.rsplit())
        pos -= 1
        if segtree[0][pos] != val:
            segtree[0][pos],aux = val,0
            for i in xrange(1,l):
                pos >>= 1
                res = segtree[i-1][pos << 1] | segtree[i-1][(pos << 1) + 1] if not aux else segtree[i-1][pos << 1] ^ segtree[i-1][(pos << 1) + 1]
                if res is segtree[i][pos]: break
                segtree[i][pos],aux = res,not aux
        ans[j] = segtree[-1][0]
    w('\n'.join(mp(st,ans)))
main()
