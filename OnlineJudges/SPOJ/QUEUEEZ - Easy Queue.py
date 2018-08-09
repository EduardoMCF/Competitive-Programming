t = int(raw_input())
fila,inicio=[],0
for i in xrange(t):
    comandos = map(int,raw_input().split())
    if comandos[0] == 1: fila.append(comandos[1])
    elif comandos[0] == 2:
        if inicio < len(fila): inicio+=1
    else:
        print fila[inicio] if inicio < len(fila) else 'Empty!'
