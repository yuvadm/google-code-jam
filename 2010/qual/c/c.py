f = open('2.in', 'r')
o = open('2.out', 'w')

t = int(f.readline().strip())

def c(l):
    while True:
        for x in l:
            yield x

for i in xrange(t):
    (r, k, n) = map(int, f.readline().strip().split(' '))
    g = map(int, f.readline().strip().split(' '))
    
    q = c(g)
    
    profit = 0
    buf = 0
    for j in xrange(r):
        load = 0
        if buf != 0:
            next = buf
            buf = 0
        else:
            next = q.next()
            
        while load + next <= k:
            load += next
            next = q.next()
        buf = next
        profit += load
    
    s = "Case #%d: %s\n" % (i+1, profit)
    o.write(s)
