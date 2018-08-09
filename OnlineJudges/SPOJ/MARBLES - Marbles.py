import time

def fat(n,k):
	f = 1
	if k>n-k:k=n-k
	for i in range(k):
		f= f*(n-i)/(i+1)
	return int(f)
n = int(raw_input())
for i in xrange(n):
    n,k=map(int,raw_input().split())
    s = time.time()
    print fat(n-1,k-1)
    t = time.time()
    print t-s