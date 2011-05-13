f = open('3.in', 'r')
o = open('3.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    N = int(f.readline().strip())
    w = [map(int, f.readline().strip().split(' ')) for _n in range(N)]
    
    w.sort(key=lambda wire: wire[0])
    
    cross = 0
    for i in range(N):
        for j in range(i+1, N):
            if w[i][1] > w[j][1]:
                cross += 1
    
    s = "Case #%d: %s\n" % (t+1, cross)
    print s
    o.write(s)
