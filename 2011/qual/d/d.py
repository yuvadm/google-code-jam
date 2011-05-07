from time import sleep

def solve(a):
    steps = 0
    sol = range(1,len(a)+1)
    # stop if solved
    while a != sol:
        print "%s is not %s" % (a, sol)
        
        # first flip all pairs
        for i in range(len(a)):
            if a[i] != i+1 and a[a[i]-1] == i+1:
                print 'flipping %d and %d' % (a[a[i]-1], a[i])
                t = a[i]
                a[i] = a[a[i]-1]
                print 'flipping %d and %d' % (a[a[i]-1], a[i])
                a[a[i]-1] = t
                print 'flipping %d and %d' % (a[a[i]-1], a[i])
                break
                steps += 2
        
        # did that suffice?
        if a == sol:
            print "%s is not %s" % (a, sol)
            break
        
        # now find the first mixed index to fix
        for i in range(len(a)):
            if a[i] != i+1:
                print 'flipping %d and %d' % (a[a[i]-1], a[i])
                a[i], a[a[i]-1] = a[a[i]-1], a[i]
                steps += 2
        sleep(1)
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