from sys import stdin,stdout
r,w=stdin.readline,stdout.write
while True:
	n = int(r())
	if not n: break
	best = [0,0]
	for i in xrange(n):
		x,y = map(int,r().split())
		size = max(min(x,y*4),max(min(x*2,y*2),min(x*4,y)))
		if size > best[0]: best[1] = i; best[0] = size 
	w(str(best[1]+1)+'\n')