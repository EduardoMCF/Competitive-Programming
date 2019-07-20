from sys import stdin,stdout
from decimal import getcontext, Decimal as D
from collections import defaultdict as dd
r,w = stdin.readline,stdout.write

n = int(r(),10)
a = map(int,r().split())
b = map(int,r().split())
count = dd(int)

max,ans = 0,0
for i in range(n):
    if not a[i] and not b[i]:
       ans += 1
    elif a[i]:
       if abs(a[i]) > 900000000 and abs(b[i]) > 900000000 and abs(abs(a[i])-abs(b[i])) == 1:
          x = D(b[i])/D(a[i])
       else:
          x = b[i]*1./a[i]
       count[x] += 1
       if count[x] > max:
           max = count[x]

w(str(max+ans))
