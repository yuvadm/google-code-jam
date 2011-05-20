f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (N, M) = map(int, f.readline().strip().split(' '))
    pe = [f.readline().strip() for _n in range(N)]
    pc = [f.readline().strip() for _m in range(M)]
    
    fs = {'' : {}}
    for p in pe:
        dirs = p.split('/')
        cur = fs
        for d in dirs:
            try:
                cur = cur[d]
            except KeyError:
                cur[d] = {}
                cur = cur[d]
    
    res = (pe, pc)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)
