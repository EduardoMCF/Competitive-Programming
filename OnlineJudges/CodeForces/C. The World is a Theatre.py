import math
def C(n,r):
    if r > n: return 0
    f = math.factorial
    return f(n)/f(r)/f(n-r)
n,m,t = map(int,raw_input().split())
s = 0
for i in xrange(4,n+1):
    if t<=i: break
    g = t-i
    s+= C(n,i)*C(m,g)
print s
