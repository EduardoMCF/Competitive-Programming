def main():
    from sys import stdin,stdout
    from bisect import bisect_left as bl
    r,w = raw_input,stdout.write

    n = int(r())
    arr = map(int,r().split())
    diffArr = [abs(arr[i]-arr[i-1]) for i in xrange(1,n)]
    qs = int(r())

    # Log preprocess
    log = [0] * (n+1)
    for i in xrange(2,n+1): log[i] = log[i//2] + 1

    # Shift preprocess
    pow = [1 << i for i in xrange(log[n]+1)]

    # build sparse table
    k = log[n]+1
    sTable = [[0]*(n+1) for i in xrange(k)]

    for i in xrange(len(diffArr)):
        sTable[0][i] = diffArr[i]

    for j in xrange(1,k+1):
        for i in xrange(n+1):
            if i + (1 << j) > n: break
            sTable[j][i] = max(sTable[j-1][i], sTable[j-1][i + pow[j-1]])

    def query(l,r):
        j = log[r-l+1]
        return maxx(sTable[j][l], sTable[j][r-pow[j]+1])

    maxx = max
    for i in xrange(qs):
        t,d = map(int,r().split())
        idx = bl(arr,t)
        idx = idx if idx < n and arr[idx] == t else idx-1
        ans,L,R = idx,0,idx-1,
        while L <= R:
            m = (L+R) >> 1;j = log[R-m+1]
            if maxx(sTable[j][m], sTable[j][R-pow[j]+1]) <= d: R = m-1;ans = m
            else: L = m+1
        w('%i\n' %(ans+1))

main()
