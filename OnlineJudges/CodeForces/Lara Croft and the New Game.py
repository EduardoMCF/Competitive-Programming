from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n,m,k = map(int,read().split())

if k < n:
    print k+1,1
elif n <= k < n+m-1:
    print n,k-n+2
else:
    k -= n
    print n - k/(m-1), m-k%(m-1) if (k/(m-1)) & 1 else k %(m-1) +2
