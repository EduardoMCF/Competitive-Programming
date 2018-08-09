def calculate(l):
	check = ans = sum = 0
	for i in xrange(n):
		for j in xrange(l[i]):
			if (i&1) ^ (j == d): continue
			ans = (ans + mt[n - i - 1][(sum + j * mod[n - i - 1]) % m]) % md
		sum = (sum + l[i]*mod[n-i-1]) % m
		if (i&1) ^ (l[i] == d): check = True;break
	if not check and not sum: ans = (ans + 1) % md
	return ans

m,d = map(int,raw_input().split()); a,b = map(int,list(raw_input())),map(int,list(raw_input()));
n,mod,md,k,mt = len(a),[0]*len(a),1000000007,1,[[0]*m for i in xrange(len(a))]
for i in xrange(n): mod[i] = k; k = (k*10) % m
mt[0][0] = 1
for i in xrange(1,n):
	for dig in xrange(10):
		if ((n-i)&1) ^ (dig == d): continue
		dif = mod[i-1]*dig
		for j in xrange(m):	mt[i][j] = (mt[i][j] + mt[i-1][(j+dif)%m]) % md
for i in xrange(n-1,-1,-1):
	if not a[i]:a[i] = 9
	else: a[i] -= 1; break
ans = calculate(b) - calculate(a)
if ans < 0: ans += md
print ans


