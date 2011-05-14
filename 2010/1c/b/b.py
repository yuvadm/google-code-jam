f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (l, p, c) = map(int, f.readline().strip().split(' '))
    
    res = 0
    if p / l != c:
        exp = 2
        res += 1
        while l * (c**exp) < p:
            exp *= 2
            res += 1
    
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
