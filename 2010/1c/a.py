f = open('3.in', 'r')
o = open('3.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    N = int(f.readline().strip())
    wires = []
    for n in range(N):
        wires.append(map(int, f.readline().strip().split(' ')))
    
    wires.sort(key=lambda wire: wire[0])
    
    cross = 0
    bw = [x[1] for x in wires]
    
    for i in range(len(bw)):
        for j in range(i+1, len(bw)):
            if bw[i] > bw[j]:
                cross += 1
    
    s = "Case #%d: %s\n" % (t+1, cross)
    print s
    o.write(s)
