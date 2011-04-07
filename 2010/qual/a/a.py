f = open('1.in', 'r')
o = open('1.out', 'w')

t = int(f.readline().strip())

for i in range(t):
    nk = f.readline().strip().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    
    a = [(0, 0)]*n
    a[0] = (1, 0)

    for j in range(k):
        for y in range(n):
            if a[y][0]==1:
                a[y] = (a[y][0], a[y][1]^1)
        
        for y in range(n):
            if y==0:
                a[y] = (1, a[y][1])
            else:
                a[y] = (a[y-1][0]*a[y-1][1], a[y][1])

#    print a[n-1][0], a[n-1][1]
    
    s = "Case #" + str(i+1) + ": OFF\n"
    if a[n-1][0]*a[n-1][1]==1:
        s = "Case #" + str(i+1) + ": ON\n"
    o.write(s)
    print s
    
