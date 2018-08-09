from sys import stdin,stdout

def toInt(list):
	return int(''.join(list))

def permute(a, l, r):
    if l==r: 
    	 candidates.append(toInt(a))
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

r,w = stdin.readline,stdout.write
n,m = r().split()
setn = set(n)
nums = list(''.join(setn))
candidates = []
permute(nums,0,len(nums)-1)

print candidates

