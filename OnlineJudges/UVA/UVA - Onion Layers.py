from sys import stdin,stdout
from operator import itemgetter
r,w=stdin.readline,stdout.write

def cross(O,A,B):
    return (A[0] - O[0]) * (B[1] - O[1]) - (A[1] - O[1]) * (B[0] - O[0])

def convexHull(P):
    H,k = [0]*(2*len(P)),0
    
    for i in xrange(len(P)):
        while (k >= 2) and (cross(H[k-2],H[k-1],P[i]) < 0): k -= 1
        H[k] = P[i]
        k += 1

    t = k + 1
    for i in xrange(len(P)-2,-1,-1):
        while (k >= t) and (cross(H[k-2],H[k-1],P[i]) < 0): k -= 1
        H[k] = P[i]
        k += 1

    return H[:k]

while True:
    n = int(r(),10)
    if not n: break
    P,l = [],0
    for i in xrange(n):
        p = map(int,r().split())
        P.append((p[0],p[1]))
    P.sort()
    while P:
        ch = convexHull(P); l+=1 ; seen = set(); Paux = []
        for i in ch: seen.add(i)
        for i in P:
            if i not in seen: Paux.append(i)
        P = Paux
    w('Take this onion to the lab!\n') if l&1 else w('Do not take this onion to the lab!\n')
