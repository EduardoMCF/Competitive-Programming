x = int(raw_input())
y = int(raw_input())

if x > y:
    maior = x
    menor = y
else:
    menor = x
    maior = y

if menor % 2 == 0:
    print sum(range(menor+1,maior,2))
else:
    print sum(range(menor+2,maior,2))
