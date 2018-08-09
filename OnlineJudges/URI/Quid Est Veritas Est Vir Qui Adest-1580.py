def factorialDP(n,m):
	factorial[0]=factorial[1]=1
   	for i in xrange(2,n+1):
   		factorial[i] = (i * factorial[i-1]) % m

def modularInverse(n):
	return pow(n,m-2,m)

def pow(x, y, m) :
	if not y: return 1
	     
	p = power(x, y / 2, m) % m
	p = (p * p) % m

	if not y % 2:
	    return p 
	else : 
	    return ((x * p) % m)

while True:
	try:
		palavra = raw_input()
		n = len(palavra)
		dicio = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,
		'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
		factorial = [0]*10000
		m = 1000000007
		for i in palavra: dicio[i]+=1
		if factorial[n]: num = factorial[n]
		else:
			factorialDP(n,m)
			num = factorial[n]
		den = 1
		for i in dicio:
			if factorial[dicio[i]]:	den *= factorial[dicio[i]]
			else:
				factorialDP(dicio[i],m)
				den *= factorial[dicio[i]]
		inv = modularInverse(den)
		res = (num*inv)%m
		print res
	except EOFError: break
