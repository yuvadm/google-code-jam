f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    _n = f.readline().strip()
    el = map(int, f.readline().strip().split(' '))
    print el
    mixed = len([el[i] for i in range(len(el)) if el[i] != i+1])
    pairs = len([el[i] for i in range(len(el)) if el[i] != i+1 and el[el[i]-1] == i+1])
    mpd = mixed - pairs
    if mpd > 0:
        mpd -= 1
    steps = pairs + (2 * mpd)
    
    res = steps
    print mixed, pairs
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)

f.close()
o.close()