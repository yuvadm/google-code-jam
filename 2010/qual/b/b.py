f = open('3.in', 'r')
o = open('3.out', 'w')

c = int(f.readline().strip())

def gcd(a, b):
    return a if b==0 else gcd(b, a % b)

for i in range(c):
    t = map(int, f.readline().strip().split(' ')[1:])
    l = [abs(x - t[0]) for x in t]
    g = reduce(gcd, l)
    
    if t[0] % g == 0:
        r = 0
    else:
        r = g - (t[0] % g)
    
    s = "Case #%d: %s\n" % (i+1, r)

    o.write(s)
