
def solve(a):
    steps = 0
    sol = range(1,len(a)+1)
    # stop if solved
    while a != sol:
        try:
            print "%s is not %s" % (a, sol)
            next = False
            # first flip all pairs
            for i in range(len(a)):
                if a[i] != i+1 and a[a[i]-1] == i+1:
                    print 'PAIR FLIP %d and %d' % (a[a[i]-1], a[i])
                    t = a[a[i]-1]
                    a[a[i]-1] = a[i]
                    a[i] = t
                    steps += 2
                    raise Exception
        
            # now find the first mixed index to fix
            for i in range(len(a)):
                if a[i] != i+1:
                    print 'FLIP %d and %d' % (a[a[i]-1], a[i])
                    t = a[a[i]-1]
                    a[a[i]-1] = a[i]
                    a[i] = t
                    steps += 2
                    raise Exception
        except:
            continue
    return steps
        

f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip()
    el = map(int, f.readline().strip().split(' '))

    print el
    res = solve(el)
    
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()