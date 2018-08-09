from sys import stdin,stdout
r,w = stdin.readline,stdout.write
n,seq = int(r(),10),r().strip()
seen = set()
d = {'R':'L','L':'R','U':'D','D':'U'}
nums = 0
for i in seq:
	if d[i] in seen:
		nums +=1
		seen = set()
	seen.add(i)
nums += 1
w(str(nums))