def main():
	from sys import stdin,stdout
	from math import sqrt
	r,w = stdin.readline,stdout.write

	def SieveOptimized(n):
		for r in xrange(2, int(sqrt(n))+1):
			for z in xrange(r*r, n+1, r):
				primeFactors[z].append(r)

	n = int(r(),10)
	seq = map(int,r().split())
	res = [0]*(100001); primeFactors = [[] for i in xrange(100001)]
	for i in xrange(2,len(primeFactors)):primeFactors[i].append(i)
	SieveOptimized(100000)

	for i in seq:
		for j in primeFactors[i]:
			res[j] += 1

	w(str(max(1,max(res))))

main()