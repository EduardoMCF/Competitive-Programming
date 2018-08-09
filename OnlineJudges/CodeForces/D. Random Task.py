def main():
	from sys import stdin,stdout
	from math import factorial as f
	r,w,res = stdin.readline, stdout.write,0; m,k= map(int,r().split())
	def Combination(p,q): return 0 if p < q  else f(p)/(f(p-q) * f(q))
	for i in xrange(64,-1,-1):
		if k <= 0: break
		combination = Combination(i,k-1)
		if combination < m:	res += (1 << (i)); m -= combination; k -= 1 ; print i ,k,combination
	w(str(res+1))
main()