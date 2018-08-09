while True:
    n= raw_input()
    c = 0
    if n == '0': break
    l = map(int,raw_input().split())
    for i in xrange(len(l)):
        if i == len(l)-1:
            if (l[i-1]<l[i]and l[i]>l[0])or(l[i-1]>l[i]and l[i]<l[0]): c+=1
        else:
            if (l[i-1]<l[i]and l[i]>l[i+1])or(l[i-1]>l[i]and l[i]<l[i+1]): c+=1
    print c

