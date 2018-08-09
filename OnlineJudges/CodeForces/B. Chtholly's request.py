zcy=[]
def czcy():
    for i in xrange(10**9):
        num =  str(i)
        if len(num)%2==0:
            if num[:len(num)/2] == num[len(num)/2:][::-1]:
                zcy.append(i)
        if len(zcy) == 10**5 +1:
            break
czcy()
print zcy
print len(zcy)
# k,p = map(int,raw_input().split())
# soma = 0
# for i in xrange(k):
#     soma += zcy[i]
# print soma%p