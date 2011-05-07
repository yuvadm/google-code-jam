f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip()
    el = map(int, f.readline().strip().split(' '))
    
    res = len([el[i] for i in range(len(el)) if el[i] != i+1])
    
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()