f = open('3.in', 'r')
o = open('3.out', 'w')

t = int(f.readline().strip())

for i in range(t):
    (n, k) = map(int, f.readline().strip().split(' '))
    
    res = 'ON' if k & 2**n-1 == 2**n-1 else 'OFF'
    
    s = "Case #%d: %s\n" % (i+1, res)

    o.write(s)
