n = int(raw_input(),10)
b = map(int,raw_input().split())
m = int(raw_input(),10)
g = map(int,raw_input().split())
p1 = p2 = c = 0
b.sort()
g.sort()
while True:
    if p1 >= n or p2 >= m: break
    if abs(b[p1]-g[p2]) == 1 or abs(b[p1]-g[p2]) == 0:
        p1+=1
        p2+=1
        c+=1
    else:
        if b[p1] < g[p2]: p1 += 1
        else: p2 += 1
print c