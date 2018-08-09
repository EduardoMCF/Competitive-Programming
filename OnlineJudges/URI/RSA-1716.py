from sys import stdin,stdout

def modInverse(a, m) :
    m0, y, x = m, 0, 1
    if (m == 1) : return 0
    while (a > 1) :
        q, t = a // m, m
        m, a, t = a % m, t, y
        y, x = x - q * y, t
    if (x < 0) :
        x = x + m0
    return x

def pow(x, y, m) :
	if not y: return 1
	     
	p = pow(x, y / 2, m) % m
	p = (p * p) % m

	if not y % 2:
	    return p 
	else : 
	    return ((x * p) % m)


r,w = stdin.readline,stdout.write
n,e,c = map(int,r().split())
d = modInverse(e,888)
w('%i\n' %pow(c,d,888))



