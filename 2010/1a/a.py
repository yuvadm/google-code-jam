f = open('1.in', 'r')
o = open('1.out', 'w')

def rotate(m):
    n = len(m)
    return [''.join([m[j][i] for j in range(n)[::-1]]) for i in range(n)]

def droprow(r):
    return '.' * r.count('.') + r.replace('.','')

def gravity(m):
    return map(droprow, m)
    
def win(m):
    win = 0
    for (i, c) in ((1, 'B'), (2, 'R')):
        win |= i
    
    return ['Neither', 'Blue', 'Red', 'Both'][win]

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    mat = [f.readline().strip() for j in range(n)]
    mat = rotate(gravity(mat))
    
    s = "Case #%d: \n%s\n" % (i+1, win(1))
    print s
    o.write(s)
