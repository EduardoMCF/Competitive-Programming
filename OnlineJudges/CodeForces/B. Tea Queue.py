from sys import stdin,stdout
r,w = stdin.readline,stdout.write
t = int(r(),10)
for i in xrange(t):
	n = int(r(),10);q = [];f = 0
	[q.append(map(int,r().split())) for k in xrange(n)]
	f = q[0][0]+1
	w(str(q[0][0]))
	for j in xrange(1,n):
		if q[j][1] < f:w(' 0')
		else: 
			f = max(q[j][0],f)
			w(' '+str(f))
			f+=1
	w('\n')	

