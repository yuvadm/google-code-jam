f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip().split(' ')
    el = map(int, f.readline().strip().split(' '))
    
    
    res = el
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)

f.close()
o.close()