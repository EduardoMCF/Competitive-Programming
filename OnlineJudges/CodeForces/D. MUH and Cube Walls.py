def main():
	from sys import stdin,stdout
	r,w = stdin.readline,stdout.write
	b,h = map(int, r().split())
	if h == 1: w(str(b)), exit()
	bears = map(int,r().split())
	horace = map(int,r().split())

	for i in xrange(len(bears)-1): bears[i] -= bears[i+1] 
	for i in xrange(len(horace)-1): horace[i] -= horace[i+1]

	b -= 1;	h -= 1;	lps = [0]*h; j = 0; length = 0;	i = 1

	# Compute
	while i < h:
		if horace[i] == horace[length]:	
			length += 1
			lps[i] = length
			i += 1
		else: 
			if length != 0: 
				length = lps[length-1]
			else: 
				lps[i] = 0 
				i += 1

	# KMP
	i = 0; counter = 0
	while i < b:
		if horace[j] == bears[i]: i += 1 ; j += 1
		if j == h: counter += 1; j = lps[j-1]
		elif i < b and horace[j] != bears[i]:
			if j != 0: j = lps[j-1]
			else: i += 1

	w(str(counter))

main()
