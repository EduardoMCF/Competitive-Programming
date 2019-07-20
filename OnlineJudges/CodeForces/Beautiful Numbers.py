from re import compile,search
a,b,n = map(int,raw_input().split())
f,pattern,res,mod = [1]*(n+1),compile('[^%s%s]' %(a,b)),0,10**9+7
for i in xrange(1,n+1):f[i] = f[i-1]*i % mod
for i in xrange(n+1): res = (res + ((f[n] * pow(f[i]%mod*f[n-i],mod-2,mod))%mod if not search(pattern,str(a*i+b*(n-i))) else 0))%mod
print res
