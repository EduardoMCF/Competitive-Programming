from sys import stdin,stdout
from collections import deque
read,write = stdin.readline,stdout.write

s = read().strip()
l = len(s)
mid = l/2 - 1 if not l%2 else l/2
left,right = mid-1,mid+1
res = [s[mid]]
while right < l or left > -1:
    if right < l:
        res.append(s[right])
        right += 1
    if left > -1:
        res.append(s[left])
        left -= 1
write(''.join(res)+'\n')
