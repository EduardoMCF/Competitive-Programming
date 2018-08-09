def main():
	from sys import stdin,stdout
	r,w = stdin.readline,stdout.write

	s = r().strip()
	size = len(s); lps = [0]*len(s); length = 0; i = 1; lpsA = [1]*len(s)

	#Compute lps
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

	maxxD = lps[-1]

	if not maxxD: w('Just a legend')
	elif maxxD in lps[:-1]: w("".join(s[:maxxD]))
	elif lps[maxxD-1]: w(''.join(s[:lps[maxxD-1]]))
	else: w ('Just a legend')

main()