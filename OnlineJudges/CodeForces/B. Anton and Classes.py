def main():
	from sys import stdin,stdout
	r,w = stdin.readline,stdout.write
	maxL1 = maxL2 = 0; minR2 = minR1 = 10**9+1

	n = int(r(),10)
	for i in xrange(n):
		L,R = map(int,r().split())
		maxL1 = max(maxL1,L);minR1 = min(minR1,R)

	m = int(r(),10)
	for i in xrange(m):
		L,R = map(int,r().split())
		maxL2 = max(maxL2,L);minR2 = min(minR2,R)

	w(str(max(maxL1 - minR2, maxL2 - minR1,0)))
main()