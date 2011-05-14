f = open('1.in', 'r')
o = open('1.out', 'w')

M1 = 0xaaaaaaaa
M0 = M1 >> 1

T = int(f.readline().strip())

for t in xrange(T):
    (M, N) = map(int, f.readline().strip().split(' '))
    grid = [int(f.readline().strip(), 16) for _m in range(M)]
    
    nextSquare = min(M, N)
    
    
    res = grid
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)
