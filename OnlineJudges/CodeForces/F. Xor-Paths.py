from sys import stdin,stdout;from collections import Counter as C
r,w = stdin.readline,stdout.write; 
n,m,k = map(int,r().split());
table = [map(int,r().split()) for i in xrange(n)]; counter = C(); res = [0]; length = (n+m-2)/2
def calculateFirstHalf(i,j,xor):
	xor ^= table[i][j]
	if i + j > length: return
	elif i + j == length: counter[(i,j,xor)] += 1
	if i < n-1: calculateFirstHalf(i+1,j,xor)
	if j < m-1: calculateFirstHalf(i,j+1,xor)
def calculateSecondHalf(i,j,xor):
	if i + j > n + m - 2 - length: return
	if i + j == n + m - 2 - length: res[0] += counter[(n-i-1,m-j-1,xor ^ k)]
	xor ^= table[n-i-1][m-j-1]
	if i < n-1: calculateSecondHalf(i+1,j,xor)
	if j < m-1: calculateSecondHalf(i,j+1,xor)
calculateFirstHalf(0,0,0),calculateSecondHalf(0,0,0)
w(str(res[0]))
