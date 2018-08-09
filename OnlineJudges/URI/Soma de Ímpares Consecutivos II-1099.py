n = int(raw_input())

for i in range(n):
    x,y = raw_input().split()
    x,y = int(x),int(y)
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    if menor % 2 ==0:
        print sum(range(menor+1,maior,2))
    else:
        print sum(range(menor+2,maior,2))
