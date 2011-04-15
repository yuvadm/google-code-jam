from itertools import product

f = open('3.in', 'r')
o = open('3.out', 'w')

n = int(f.readline().strip())

for i in range(n):
    l = f.readline().strip()
    res = ' '.join(l.split(' ')[::-1])
    s = "Case #%d: %s\n" % (i+1, res)
    o.write(s)
