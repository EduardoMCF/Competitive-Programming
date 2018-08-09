from sys import stdin,stdout
from math import log
r,w = stdin.readline,stdout.write
def sparse(n):
	for j in xrange(1,n):
		if (1 << j) > n: break
		for i in xrange(0,n):
			if i + (1 << j)-1 >= n: break
			sparse_table[i][j] = min(sparse_table[i][j-1], sparse_table[i + (1 << (j-1))][j-1])

def query(l,r):
	j=int(log(r-l+1,2))
	return min(sparse_table[l][j],sparse_table[r-(1<<j)+1][j])

n = int(r(),10)
a = map(int,r().split())
c = map(int,list(r().strip()))
sparse_table = [[0]*(int(log(n-1,2))+1) for i in xrange(n-1)]
for i in xrange(n-1): sparse_table[i][0] = c[i]
sparse(n-1)

for i in xrange(n):
	if a[i] != i+1:
		if a[i] < i+1:
			if not query(a[i]-1,i-1):
				w('NO')
				exit()
		else:
			if not query(i,a[i]-2):
				w('NO')
				exit()
w('YES')
