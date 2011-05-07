f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip()
    el = map(int, f.readline().strip().split(' '))
    print el
    m = len([el[i] for i in range(len(el)) if el[i] != i+1 and el[el[i]-1] != i+1])
    p = len([el[i] for i in range(len(el)) if el[i] != i+1 and el[el[i]-1] == i+1])

    if m > 0:
        m -= 1
    steps = p + (2 * m)
    
    res = steps
    print m, p
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()