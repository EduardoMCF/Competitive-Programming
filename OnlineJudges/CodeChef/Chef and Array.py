from math import log
from sys import stdin,stdout

def sparse(array,n):
	for j in xrange(1,n):
		if 1<<j > n: break
		for i in xrange(0,n):
			if i + (1<<j) - 1 >= n: break 
			sparse_table[i][j] = max(sparse_table[i][j-1], sparse_table[i + (1<<(j-1))][j-1])
 
def query(l,r):
	j = int(log(r-l+1,2),10)
	return max(sparse_table[l][j], sparse_table[r - (1<<j) + 1][j])
 
n = input()
array = map(int,stdin.readline().split())
m,x,y = map(int,stdin.readline().split())
 
sparse_table = [[0]*(int(log(n,2))+1) for i in xrange(n)]
for i in xrange(n): sparse_table[i][0] = array[i]
sparse(array,n)
 
ans = query(min(x,y),max(x,y))
for i in xrange(1,m):
	x = (x+7) % (n-1)
	y = (y+11) % n
	ans += query(min(x,y),max(x,y))
 
stdout.write(str(ans)+'\n')

