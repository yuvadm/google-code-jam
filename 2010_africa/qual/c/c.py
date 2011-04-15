f = open('3.in', 'r')
o = open('3.out', 'w')

D = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def t9(s):
    if s==' ':
        return '0'
    for i in D:
        try:
            t = i.index(s) + 1
            return str(D.index(i) + 2) * t
        except:
            continue
    return s


n = int(f.readline().strip())

for m in range(n):
    l = f.readline()
    
    if l != '':
        c = [t9(x) for x in l]
        res = c[0]
    
        for (a,b) in [(c[i], c[i+1]) for i in range(len(c)-1)]:
            if a[0] == b[0]:
                res += ' '
            res += b
    else:
        res = ''
    
    s = "Case #%d: %s\n" % (m+1, res)
    print s
    o.write(s)
