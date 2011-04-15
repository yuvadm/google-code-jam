f = open('1.in', 'r')
o = open('1.out', 'w')

def cols(m):
    n = len(m)
    return [''.join([m[j][i] for j in range(n)]) for i in range(n)]

def diag(m):
    n = len(m)
    d = [zip(range(i+1) ,range(i+1)[::-1]) for i in range(n)]
    print d
    return [''.join([m[i][j] for (i,j) in diag]) for diag in d]
    
def diag_inv(m):
    n = len(m)
    d = [zip(range(i+1),range(i+1)[::-1]) for i in range(n)]
    return [''.join([m[n-1-i][j] for (i,j) in diag]) for diag in d]

# still need the bottom triangles!!!!! ^^^^^

def rotate(m):
    n = len(m)
    return [''.join([m[j][i] for j in range(n)[::-1]]) for i in range(n)]

def droprow(r):
    return '.' * r.count('.') + r.replace('.','')

def gravity(m):
    return map(droprow, m)

def winrow(r, k):
    res = 0
    if r.find('B'*k) != -1:
        res |= 1
    if r.find('R'*k) != -1:
        res |= 2
    return res

def win(m, k):
    R = ['Neither', 'Blue', 'Red', 'Both']
    win = 0
    for row in m:
        win |= winrow(row, k)
    for col in cols(m):
        win |= winrow(col, k)
    
    return R[win]

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    mat = [f.readline().strip() for j in range(n)]
    mat = rotate(gravity(mat))
    
    s = "Case #%d: \n%s\n" % (i+1, win(1))
    print s
    o.write(s)
