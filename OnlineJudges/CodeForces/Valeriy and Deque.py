from sys import stdin,stdout
from collections import deque
read,write = stdin.readline,stdout.write
n,q = map(int,read().split())
arr = map(int,read().split())
dq = deque(arr)
if q:
    queries = [int(read()) for _ in xrange(q)]
    pos = arr.index(max(arr))
    maxi = arr[pos]
    res = []
    for i in xrange(1,pos+1):
        a,b = dq.popleft(), dq.popleft()
        dq.appendleft(max(a,b)), dq.append(min(a,b))
        res.append((a,b))
    dq.popleft()
    newArr = [dq.popleft() for i in xrange(n-1)]
    [write('%i %i\n' %((maxi,newArr[(i-pos-1)%(n-1)]) if i > pos else  res[i-1])) for i in queries]

