while True:
    try:
        x = y = deuMerda = 0
        s=raw_input()
        for i in s:
            if i == "(": x+=1
            if i == ")": y+=1
            if y>x:
                deuMerda = True
                break
        print "correct" if (x == y and not deuMerda) else "incorrect"
    except EOFError: break