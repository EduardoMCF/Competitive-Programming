from sys import stdin,stdout
read,write = stdin.readline,stdout.write

termial = lambda x: (x**2 + x) / 2
k,n,w = map(int,read().split())
write('%i' %(max(termial(w)*k-n,0)))
