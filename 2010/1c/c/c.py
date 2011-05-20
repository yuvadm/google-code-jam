f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (M, N) = map(int, f.readline().strip().split(' '))
    grid = [bin(int(f.readline().strip(), 16))[2:] for _m in range(M)]
    
    nextSquare = min(M, N)
    
    
    res = '\n'.join([x for x in grid])
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)
