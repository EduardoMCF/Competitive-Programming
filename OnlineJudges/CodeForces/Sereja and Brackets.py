def main():
    from sys import stdin,stdout
    from collections import deque
    rr,w,it,mp,st = stdin.readline,stdout.write,int,map,str

    arr = stdin.next().rstrip()
    n = len(arr)
    q = it(stdin.next())
    queries = [[] for _ in xrange(n+1)]
    ans = [0]*q

    #Build
    bit = [0]*(n+1)
    for idx,line in enumerate(stdin):
        l,r = mp(it,line.split())
        queries[r-1].append((l-1,r-1,idx))

    stack = deque()
    for j in xrange(n):
        if arr[j] == '(':
            stack.appendleft(j)
        else:
            if stack:
                i = stack.popleft() + 1
                while i <= n: bit[i] += 1; i += (i & (-i))

        for l,r,idx in queries[j]:
            i,k = j+1,l
            s1 = s2 = 0
            while i>0 or k>0:
                if i > 0: s1 += bit[i]; i -= i & (-i)
                if k > 0: s2 += bit[k]; k -= k & (-k)
            ans[idx] = (s1-s2) << 1

    w('\n'.join(mp(st,ans)))

main()
