s = raw_input().lower()
ns = ''
vowels = ["A","O","Y","E","I","U","a","e","i","o","u","y"]
for i in s:
    if i not in vowels: ns += ' %s' %i
print ns.replace(' ','.')
