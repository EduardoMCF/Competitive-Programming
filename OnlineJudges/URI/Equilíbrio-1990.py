from sys import stdin,stdout

while True:
	n = input()
	if n == -1: break
	arr = map(int,stdin.readline().split())
	vistos = set(arr)
	arr.sort()
	soma,res = sum(arr),0
	l,r = (n-2)/2, (n-1)/2

	if arr[r] - arr[l] - 1:
		sol = soma/(n-1)
		if sol == int(sol) and sol not in vistos and arr[l] < sol < arr[r] and (sol+soma)/n == sol: res += 1

	if l < len(arr):
		sol = arr[l]*n - soma
		if -10**15 < sol < arr[l] and sol == int(sol) and sol not in vistos and (sol+soma)/n == arr[l]: res += 1

	if r < len(arr) :
		sol = arr[r]*n - soma
		if arr[r] < sol < 10**15 and sol == int(sol) and sol not in vistos and (sol+soma)/n == arr[r]: res += 1

	stdout.write(str(res)+'\n')