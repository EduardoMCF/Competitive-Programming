from sys import stdin,stdout
from math import ceil
from collections import defaultdict
r,w=stdin.readline,stdout.write

def cross_product(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def distance(a, b): return ((a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]))**0.5;

def height(a, b, c) : return abs(cross_product(a, b, c) / distance(a, b));

def _myDet(p, q, r): return (q[0]*r[1] + p[0]*q[1] + r[0]*p[1]) - (q[0]*p[1] + r[0]*q[1] + p[0]*r[1])

def _isRightTurn(s): return 1 if _myDet(s[0], s[1], s[2]) < 0 else 0

def convexHull(P):
    points = P
    points.sort()

    upper = [points[0], points[1]]
    for p in points[2:]: 
        upper.append(p)
    	while len(upper) > 2 and not _isRightTurn(upper[-3:]): del upper[-2]

    points.reverse()
    lower = [points[0], points[1]]
    for p in points[2:]: 
        lower.append(p)
    	while len(lower) > 2 and not _isRightTurn(lower[-3:]): del lower[-2]

    del lower[0]
    del lower[-1]

    t = tuple(upper+lower)
    for i in t: dic[i] = 0
    return t

c=0
n = int(r(),10)
P = [map(int,r().split()) for i in xrange(n)]
dict = defaultdict(int)
hull = convexHull(P)
print hull
# while True:
#     n = int(r(),10)
#     if not n: break
#     P = [map(int,r().split()) for i in xrange(n)]
#     hull = convexHull(P); d = float('inf'); c += 1
#     for i in xrange(len(hull)):
#         j,m = (i+1) % len(hull),0
#         for k in xrange(len(hull)):
#             m = max(m,height(hull[i],hull[j],hull[k]))
#         d = min(d,m)
#     w('Case %i %.2f\n' %(c,ceil(d*100)/100))