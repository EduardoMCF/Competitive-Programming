def main():
    from sys import stdin,stdout
    from collections import defaultdict as dd
    r,rr,w = stdin.readline,stdin.readlines,stdout.write

    n = int(r())
    arr = map(int,r().split())
    qs = int(r())

    def gcd(a, b):
        while b: a %= b; a,b = b,a
        return a

    # Log preprocess
    log = [0] * (n+1)
    CACHESHIFTR = [i >> 1 for i in xrange(2*(n+1))]
    for i in xrange(2,n+1):
        log[i] = log[CACHESHIFTR[i]] + 1

    # ShiftL preprocess
    pow = [1 << i for i in xrange(log[n]+2)]

    # build sparse table
    k = log[n]+1
    sTable = [[0]*(n+1) for i in xrange(k)]

    for i in xrange(n):
        sTable[0][i] = arr[i]

    for j in xrange(1,k+1):
        for i in xrange(n+1):
            if i + pow[j] > n: break
            sTable[j][i] = gcd(sTable[j-1][i], sTable[j-1][i + pow[j-1]])

    res = dd(int)
    it = int
    for i in xrange(n):
        ant,value = i,arr[i]
        while ant < n:
            L,R,prox,nextVal = ant,n-1,n,1
            while L <= R:
                s = L+R
                m = CACHESHIFTR[s]
                j = log[m-i+1]
                q = gcd(sTable[j][i], sTable[j][m-pow[j]+1])
                if q < value: R = m-1; nextVal = q; prox = m
                else: L = m+1
            res[value] += prox-ant
            ant,value = prox,nextVal
    #[w('%i\n' %res[int(r(),10)]) for i in xrange(qs)]
    w(''.join('%i\n' %res[i] for i in map(it,rr())))
main()
