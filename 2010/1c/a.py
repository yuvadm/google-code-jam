f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    N = int(f.readline().strip())
    wires = []
    for n in range(N):
        wires.append(map(int, f.readline().strip().split(' ')))
    
    wires.sort(key=lambda wire: wire[0])
    
    cross = 0
    bwires = [x[1] for x in wires]
    print bwires
    bwd = [bwires[i+1]-bwires[i] for i in range(len(bwires)-1)]
    print bwd
    res = len([x for x in bwd if x < 0])
    
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    #o.write(s)
