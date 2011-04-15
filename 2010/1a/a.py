f = open('1.in', 'r')
o = open('1.out', 'w')

t = int(f.readline().strip())

for i in range(t):
    nk = f.readline().strip().split(' ')
    
    s = "Case #%d: %s\n" % (i+1, res)

    o.write(s)
