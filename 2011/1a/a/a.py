f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (N, PD, PG) = map(int, f.readline().strip().split(' '))
    res = 'Possible' if PD > PG else 'Broken'
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
