from sys import stdin,stdout
r,w = stdin.readline,stdout.write
s1,s2,d,ans = r().strip(),r().strip(),{},[]
for i in xrange(len(s1)):
	if s1[i] in d:
		if d[s1[i]] != s2[i]:
			w('-1')
			exit()
	if s2[i] in d:
		if d[s2[i]] != s1[i]:
			w('-1')
			exit()
	else:
		d[s1[i]]=s2[i]
		d[s2[i]]=s1[i]
		if s1[i] != s2[i]:ans.append((s1[i],s2[i]))

w(str(len(ans))+'\n')
for k,v in ans:	w(k+' '+v+'\n')