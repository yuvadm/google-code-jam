

f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip()
    el = map(int, f.readline().strip().split(' '))

    m = len([el[i] for i in range(len(el)) if el[i] != i+1 and el[el[i]-1] != i+1])
    p = len([el[i] for i in range(len(el)) if el[i] != i+1 and el[el[i]-1] == i+1])
    
    print m, p
    m = m-1 if m > 0 else 0
    res = p + (m * 2)
    
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()