def main():
	from sys import stdin,stdout
	from math import atan2
	r,w=stdin.readline,stdout.write
	n = int(r())
	vectors = [map(int,r().split())+[i] for i in xrange(n)]
	vectors.sort(key = lambda vec: atan2(vec[1],vec[0]))
	vectors.append(vectors[0])
	dx,dy = vectors[0][0]*vectors[1][0] + vectors[0][1]*vectors[1][1],abs(vectors[0][0]*vectors[1][1]-vectors[1][0]*vectors[0][1])
	minx,miny,minn,minn1 = dx,dy,vectors[0][2],vectors[1][2]
	for i in xrange(1,len(vectors)):
		dx1,dy1 = vectors[i-1][0]*vectors[i][0]+vectors[i-1][1]*vectors[i][1],abs(vectors[i-1][0]*vectors[i][1]-vectors[i][0]*vectors[i-1][1])
		if dx1*miny-dy1*minx>0: minn,minn1,minx,miny = vectors[i-1][2],vectors[i][2],dx1,dy1 
	w(str(minn+1)+' '+str(minn1+1))
main()