from itertools import product

f = open('3.in', 'r')
o = open('3.out', 'w')

n = int(f.readline().strip())

for j in range(n):
    c = int(f.readline().strip())
    i = int(f.readline().strip())
    P = map(int, f.readline().strip().split(' '))
    
    res = (0, 0)
    for k in range(len(P)):
        for l in range(k+1, len(P)):
            if P[k]+P[l]==c:
                res = [k+1, l+1]
                res = ' '.join(map(str, res))
                break
    
    s = "Case #%d: %s\n" % (j+1, res)
    
    o.write(s)
