f = open('1.in', 'r')
o = open('1.out', 'w')

n = int(f.readline().strip())

for j in range(n):
    c = int(f.readline().strip())
    i = int(f.readline().strip())
    P = map(int, f.readline().strip().split(' '))
    
    s = "Case #%d: %s\n" % (j+1, P)
    
    print s
    o.write(s)
