def main():
	from sys import stdin,stdout
	r,w = stdin.readline,stdout.write
	k,n = int(r(),10), map(int,list(r().strip()))
	n.sort(); dig = 0; som = sum(n)
	for i in n:
		if som < k: som += 9 - i; dig += 1
	w(str(dig))
main()
