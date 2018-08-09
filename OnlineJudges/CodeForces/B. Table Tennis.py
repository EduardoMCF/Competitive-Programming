n,k = map(int,raw_input().split())
e = map(int,raw_input().split())
M = max(e)
if k >= n:print M
else:
    for i in xrange(n):
        c, a, achou = 0, 1, False
        if e[i] == M:
            print M
            break
        while e[i] >= e[i+a]:
			if i+a == n:a = 0
			a+=1
			c+=1
			if c == k:
                achou=True
                break
        if achou:
			print e[i]
            break