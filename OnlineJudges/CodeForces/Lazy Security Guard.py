from math import ceil
n = input()
mini = 10**6+1
for x in xrange(1,n+1): mini = min(mini,2*(x+int(ceil(n*1./x))))
print mini
