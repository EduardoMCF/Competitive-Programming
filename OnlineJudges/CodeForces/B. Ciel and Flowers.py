r,g,b = map(int,raw_input().split())
checklist = [r,g,b]
vaitiltar = True
if 0 in checklist: vaitiltar=False
sR,sG,sB = r%3,g%3,b%3
nR,nG,nB = r/3,g/3,b/3
l=[sR,sG,sB]
l.sort()
mix = min(sR,sG,sB)
if l == [0,2,2] and vaitiltar: mix=1
print nR+nG+nB+mix