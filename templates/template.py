f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (n, m, o) = map(int, f.readline().strip().split(' '))
    l = f.readline().strip()
    
    res = str(n) + str(m) + str(o) + l
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)
