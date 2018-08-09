n,m,a,b = map(int,raw_input().split())
t,v,r = b/m,0,a*(n%m)
if t < a:
    if r < b: mini = r
    else: mini = b
    v = n/m*b + mini
else:
    v = n*a
print v

