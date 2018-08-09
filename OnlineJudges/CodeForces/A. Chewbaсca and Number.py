n = raw_input()
r = ''
k = ''
for i in n[1:]:
    if int(i) >= 5:r.join(str(9-int(i)))
    else: r.join(i)
if 5 <= int(n[0]) < 9:
    k.join(str(9-int(n[0])))
    print k+r
else:
    print n[0]+r