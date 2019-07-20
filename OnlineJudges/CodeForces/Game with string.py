from sys import stdin,stdout;from itertools import count
r,w = stdin.readline,stdout.write
aux,res = [],count()
[aux.append(c) if not aux or c is not aux[-1] else (next(res),aux.pop()) for c in r().strip()]
w('NO' if not next(res) & 1 else 'YES')
