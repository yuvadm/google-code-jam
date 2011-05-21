f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (N, PD, PG) = map(int, f.readline().strip().split(' '))
    
    wt = (N * PD)
    wy = (N * PG)
    
    print (wt, wy)
    
    res = 'Possible' if PD >= PG else 'Broken'
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
