print(sum(max([tuple(map(int,raw_input().split())) for i in xrange(input())],key=lambda x: sum(x))))
