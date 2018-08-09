while True:
    try:
        frase = raw_input()
        p = ac = ""
        inicio = False
        for i in frase:
            if i == '[': inicio, p, ac = True, ac + p, ''
            if i == ']': inicio, p, ac = False, ac + p, ''
            if inicio and i != '[':ac += i
            if not inicio and i != ']':p += i
        print ac + p
    except EOFError:break