f = open('3.in', 'r')
o = open('3.out', 'w')

T = int(f.readline().strip())

xor = lambda x,y: x^y

for t in xrange(T):
    _n = f.readline().strip().split(' ')
    C = map(int, f.readline().strip().split(' '))

    s, p = C, []
    s.sort()
    s.reverse()
    
    p.append(s.pop())
    
    res = 'NO'
    while s:
        ss = reduce(xor, s)
        sp = reduce(xor, p)
        if ss == sp:
            res = str(sum(s))
            break
        p.append(s.pop())
    
    s = "Case #%d: %s\n" % (t+1, res)
    #print s
    o.write(s)

f.close()
o.close()