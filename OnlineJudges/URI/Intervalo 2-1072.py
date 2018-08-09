n = int(raw_input())
x_in = 0
x_out = 0
for i in range(n):
    x = int(raw_input())
    if 10 <= x <= 20:
        x_in += 1
    else:
        x_out += 1

print x_in,'in'
print x_out,'out'