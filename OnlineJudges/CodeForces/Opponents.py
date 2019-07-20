from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n,d = map(int,read().split())
days = [int(read().strip(),2) for _ in xrange(d)]
lose = 2**n-1
c=res=0
for day in days:
    c += 1 if day != lose else -c;
    res = max(res,c)
write(str(res))
