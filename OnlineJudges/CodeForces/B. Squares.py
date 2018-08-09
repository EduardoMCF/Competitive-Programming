n,k=map(int,raw_input().split())
l = map(int,raw_input().split())
l.sort(reverse=True)
if k <= n: print l[k-1],0
else: print -1