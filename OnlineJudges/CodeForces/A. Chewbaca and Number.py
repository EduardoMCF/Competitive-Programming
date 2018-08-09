n = raw_input()
n0 = n[0]
r = ''
k = ''
for i in n[1:]:
    if int(i) >= 5:r += str(9-int(i))
    else: r += i
if 5 <= int(n0) < 9:
    k =(str(9-int(n0)))
    print k+r
else:
    print n0+r