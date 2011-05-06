f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    s = "Case #%d: %s\n" % (t+1, res)
    #print s
    o.write(s)

f.close()
o.close()