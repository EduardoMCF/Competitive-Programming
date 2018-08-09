n,s = raw_input().split()
def msmdez(x,y):
	x,y = int(x),int(y)
	x1,y1 = str(x),str(y)
	if len(x1) == len(y1) != 1:
		if abs(x-y) < 10:
			return x1[-2] == y1[-2]
	return False
md = msmdez(n,s)
if int(n) <= int(s):
	print 0
	exit()
if int(n) < int(s) + sum(map(int,list(n))) and not md:
	print 0
	exit()
n,s = int(n),int(s)
if s < 10 :
	print n - 10 + 1
	exit()
if md:
	print 0
	exit()
S = s
while S <= n and not msmdez(S,n):
	k = S - sum(map(int,list(str(S))))
	if k >= s: break
	S+=10 
if S - sum(map(int,list(str(S)))) < s:
	print int(str(n)[-1]) + 1
	exit()
print n  - (S - int(str(S)[-1])) + 1



