from math import log
k,l = input(),input()
res = round(log(l,k),12)
print 'YES\n%i' %(res-1) if res.is_integer() else 'NO'

