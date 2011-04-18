f = open('1.in', 'r')
o = open('1.out', 'w')

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    mat = [f.readline().strip() for j in range(n)]
    mat = rotate(gravity(mat))

    s = "Case #%d: %s\n" % (i+1, win(mat, k))
    print s
    o.write(s)
