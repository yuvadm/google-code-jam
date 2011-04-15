f = open('1.in', 'r')
o = open('1.out', 'w')

# rotate *90 degrees clockwise*
def rotate(m):
    n = len(m)
    return [''.join([m[j][i] for j in range(n)[::-1]]) for i in range(n)]

# drop a single row
def droprow(r):
    return '.' * r.count('.') + r.replace('.','')

# drop the rotated matrix
def gravity(m):
    return map(droprow, m)

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    mat = [f.readline().strip() for j in range(n)]
    res = rotate(gravity(mat))
    
    s = "Case #%d: \n%s\n" % (i+1, '\n'.join(res))
    print s
    o.write(s)
