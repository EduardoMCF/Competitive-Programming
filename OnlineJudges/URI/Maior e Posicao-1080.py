n_m = 0
for i in range(1,101):
    n = int(raw_input())
    if n > n_m:
        n_m = n
        pos = i
print n_m
print pos