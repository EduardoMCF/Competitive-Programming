from sys import stdin,stdout
from fractions import gcd
read,write = stdin.readline,stdout.write

n = int(read())
pairs = [map(int,read().split()) for _ in xrange(n)]

res = 0
for a,b in pairs:  res = gcd(a*b,res)

for a,b in pairs: gcdA,gcdB = gcd(res,a),gcd(res,b); res = gcdA if gcd(res,a) != 1 else gcdB

write(str(res) if res != 1 else '-1')
