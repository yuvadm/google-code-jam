f = open('2.in', 'r')
o = open('2.out', 'w')

def cols(m):
    n = len(m)
    return [''.join([m[j][i] for j in range(n)]) for i in range(n)]

def diag(m):
    n = len(m)
    d = [zip(range(i+1) ,range(i+1)[::-1]) for i in range(n)]
    d += [zip(range(i+1, n) ,range(i+1, n)[::-1]) for i in range(n-1)]
    return [''.join([m[i][j] for (i,j) in diag]) for diag in d]
                                           
def diag_inv(m):
    n = len(m)
    d = [zip(range(i+1),range(i+1)[::-1]) for i in range(n)]
    d += [zip(range(i+1, n) ,range(i+1, n)[::-1]) for i in range(n-1)]
    return [''.join([m[n-1-i][j] for (i,j) in diag]) for diag in d]

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
    for dia in diag(m):
        win |= winrow(dia, k)
    for idia in diag_inv(m):
        win |= winrow(idia, k)
    return R[win]

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    mat = [f.readline().strip() for j in range(n)]
    mat = rotate(gravity(mat))

    s = "Case #%d: %s\n" % (i+1, win(mat, k))
    print s
    o.write(s)
