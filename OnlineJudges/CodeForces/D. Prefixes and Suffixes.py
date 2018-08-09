def main():
	from sys import stdin,stdout
	r,w = stdin.readline,stdout.write

	s = r().strip()
	size = len(s); lps = [0]*len(s)

	if len(set(s)) == 1:
		w(str(size)+'\n')
		for i in xrange(size):
			w('%i %i\n' %(i+1,size-i))
		exit()

	#Compute lps
	length = 0; i = 1;
	while i < size :
		if s[i] == s[length]:	
			length += 1
			lps[i] = length
			i += 1
		else: 
			if length != 0: 
				length = lps[length-1]
			else: 
				lps[i] = 0 
				i += 1

	maxPS = lps[-1]; validStr = []

	while maxPS > 0:
		validStr.append(maxPS);	maxPS = lps[maxPS-1]

	freq = [1]*size

	for i in xrange(-1,-len(lps)-1,-1):
		if lps[i]: freq[lps[i]-1] += freq[i]

	w(str(len(validStr)+1)+'\n')
	for i in reversed(validStr): w('%i %i\n' %(i,freq[i-1]))
	w('%i 1' %(len(s)))
	
main()