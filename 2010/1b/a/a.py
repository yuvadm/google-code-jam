f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    (N, M) = map(int, f.readline().strip().split(' '))
    pe = [f.readline().strip() for _n in range(N)]
    pc = [f.readline().strip() for _m in range(M)]
    
    res = 0
    fs = {'' : {}}
    for paths in (pe, pc):
        for p in paths:
            dirs = p.split('/')
            cur = fs
            for d in dirs:
                try:
                    cur = cur[d]
                except KeyError:
                    cur[d] = {}
                    cur = cur[d]
                    if paths == pc:
                        res += 1
    
    s = "Case #%d: %d\n" % (t+1, res)
    print s
    #o.write(s)
