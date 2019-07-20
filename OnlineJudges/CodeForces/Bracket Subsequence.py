from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n,k = map(int,read().split())
sequence = read().strip()
c = 0
for i,bracket in enumerate(sequence):
    if bracket == '(':
        c += 1
    if c == k/2: break
    #print i

write(sequence[:i+1]+')'*(k-(i+1)))
