def main():
	from sys import stdin,stdout,__stdout__
	from collections import defaultdict
	from io import BytesIO
	from atexit import register
	from multiprocessing import Pool
	buffer = BytesIO()
	stdout = buffer
	p = Pool(2)
	def make_set(a):parent[a],rank[a] = a,1
	def find(a):
		if a==parent[a]: return a
		parent[a]=find(parent[a])
		return parent[a]
	def union(a,b):
		parentA,parentB=find(a),find(b)
		if parentA==parentB: return
		if rank[parentA] > rank[parentB]:parent[parentB],rank[parentA]=parentA, rank[parentA]+rank[parentB]
		else:parent[parentA],rank[parentB]=parentB,rank[parentB]+rank[parentA]
	@register
	def write():__stdout__.write(buffer.getvalue())
	def cond(x,y):
		x,y = int(x,10),int(y,10)
		if not parent[x]: make_set(x)
		if not parent[y]: make_set(y)
		union(x,y)
	def build():
		[[ cond(x,y) for x,y in r().split()] for i in xrange(m)]
	parent,rank = defaultdict(int),defaultdict(int)
	r,w,mk,f,u = stdin.readline,stdout.write,make_set,find,union
	while True:
		try:
			n,m = p.map(int,r().split())
			p.build()
			q = int(r(),10)
			if not parent[q]: w('1\n')
			else: w('%s\n' %str(rank[f(q)]))
		except EOFError: break
main()