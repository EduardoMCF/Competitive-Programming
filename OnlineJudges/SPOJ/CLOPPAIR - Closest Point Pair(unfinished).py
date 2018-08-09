from sys import stdin,stdout,setrecursionlimit
setrecursionlimit(10000)
r,w=stdin.readline,stdout.write

def calculate(px,py,n):
	if n <= 3:
		minnn,index = float("inf"),[0,0]
		for i in xrange(n):
			for j in xrange(i+1,n):
				dist = ((px[i][0] - px[j][0])*(px[i][0] - px[j][0]) + (px[i][1] - px[j][1])*(px[i][1] - px[j][1]))**0.5
				if dist < minnn: minnn = dist;coord[0],coord[1] = i,j
		return minnn

	m = n/2
	mP = px[m]
	pyl,pyr,li,ri = [0]*(m+1),[0]*(n-m-1),0,0
	for i in xrange(n):
		if py[i][0] <= mP[0]: pyl[li] = py[i]; li += 1
		else: pyr[ri] = py[i]; ri += 1

	d = min(calculate(px,pyl,m),calculate(px,pyr,n-m))

	strip,j = [0]*n,0
	for i in xrange(n):
		if abs(py[i][0] - mP[0]) < d: strip[j] = py[i]; j += 1

	minn = d
	for i in xrange(j):
		for k in xrange(i+1,j):
			if not (strip[k][1] - strip[i][1] < minn): break
			dist1 = ((strip[i][0] - strip[k][0])*(strip[i][0] - strip[k][0]) + (strip[i][1] - strip[k][1])*(strip[i][1] - strip[k][1]))**0.5
			if dist1 < minn:
				minn = dist1;coord[0],coord[1] = i,k

	
	return min(d,minn)

n = int(r())
coord,px,py,m = [0,0],[],[],map
for i in xrange(n):
	x,y = m(int,r().split())
	px.append((x,y)),py.append((x,y))
px.sort(key = lambda x: x[0]),py.sort(key = lambda x: x[1])
print coord
w(str(calculate(px,py,n)))


