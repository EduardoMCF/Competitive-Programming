s = raw_input()
b = 'Bulbasr'
l = [0,0,0,0,0,0,0]
c = True
for j in range(len(b)):
    for i in range(len(s)):
        if s[i] == b[j]:
            l[j]+=1
l[1] /= 2
l[4] /= 2
for k in l:
    if k < min(l):c=False
if c==True:print min(l)

