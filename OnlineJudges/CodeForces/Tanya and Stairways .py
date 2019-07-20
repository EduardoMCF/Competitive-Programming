from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n = int(read())
stairs = read().split()

positions = [i for i,v in enumerate(stairs) if v == '1']
positions.append(n)
write('%i\n' %(len(positions)-1))
for i in xrange(len(positions)-1):
    write('%i ' %(positions[i+1]-positions[i]))
