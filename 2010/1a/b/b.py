f = open('1.in', 'r')
o = open('1.out', 'w')

def smooth(a, d, i, m):
    if len(a) <= 1:
        return 0
    if abs(a[0]-a[1]) > m:
        cd = d + smooth(a[1:], d, i, m)
        ci = i + smooth(a[1:], d, i, m)
        cc = c
        return min(cd, ci, cc) + smooth(a[1:], d, i, m)
    else:
        return smooth(a[1:], d, i, m)

T = int(f.readline().strip())

for t in range(T):
    (d, i, m, _n) = map(int, f.readline().strip().split(' '))
    A = map(int, f.readline().strip().split(' '))
    r = smooth(A, d, i, m)
    s = "Case #%d: %s\n" % (t+1, r)
    print s
    o.write(s)
