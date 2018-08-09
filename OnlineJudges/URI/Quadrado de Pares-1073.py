n = int(raw_input())
if n % 2 == 0 :
    for i in range(2,n+1,2):
        print '%i^2 = %i' %(i,i**2)
else:
    for i in range(2,n,2):
        print '%i^2 = %i' %(i,i**2)