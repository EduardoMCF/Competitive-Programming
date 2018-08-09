def main():
	from sys import stdin,stdout
	from math import pi
	r,w=stdin.readline,stdout.write
	n,x,y = map(int,r().split())
	points = [map(int,r().split()) for i in xrange(n)]
	maxD,minD = 0,10000000
	for i in xrange(n):
		distance = ((abs(x-points[i][0]))**2 + (abs(y-points[i][1]))**2)**(1/2.)
		if distance > maxD:	maxD = distance 
		if distance < minD: minD = distance
	for i in xrange(n):
		p1,p2 = points[i],points[(i+1)%n]
		px = p2[0]-p1[0]; py = p2[1]-p1[1]
		u = ((x-p1[0])*px + (y-p1[1])*py)/((px*1.)**2 + (py*1.)**2)
		if u > 1: u = 1
		if u < 0: u = 0
		x1 = p1[0] + u*px; y1 = p1[1] + u*py
		dx = x1 - x; dy = y1 - y
		distance = (dx*dx + dy*dy)**(0.5)
		if distance > maxD:	maxD = distance 
		if distance < minD: minD = distance
	minA = pi*(minD)**2
	maxA = pi*(maxD)**2
	w(str(maxA-minA))
main()