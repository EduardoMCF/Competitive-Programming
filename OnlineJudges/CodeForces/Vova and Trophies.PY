from sys import stdin,stdout
read,write = stdin.readline,stdout.write

def customSplit(s):
    n = len(s)
    c = qtd = 0
    ans = []
    while c < n:
        if s[c] == 'G':
            qtd += 1
        else:
            qtd = 0
        ans.append(qtd)
        c+=1
    return ans

n = int(read())
s = read().strip()
if set(s) == {'G'}:
    print n
else:
    auxLeft,auxRight = customSplit(s),customSplit(s[::-1])[::-1]
    ans = 0
    func = lambda i: (auxLeft[i-1] if i>0 else 0) + (auxRight[i+1] if i+1 < n else 0)
    for i,v in enumerate(s):
        ans = max(ans,func(i)+1 if v == 'S' else 0)
    ans = min(ans,s.count('G'))
    print ans
