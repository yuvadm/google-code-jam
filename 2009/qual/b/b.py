f = open('1.in', 'r')
o = open('1.out', 'w')

B = [chr(ord('a')+i) for i in xrange(26)]

t = int(f.readline().strip())

for case in xrange(t):
    hw = f.readline().strip().split(' ')
    h = int(hw[0])
    w = int(hw[1])
    
    m = [map(int, f.readline().strip().split(' ')) for j in xrange(h)]
    
    cb = 0
    bm = [['-']*h]*w
    bm[0][0] = B[cb]
    
    for i in xrange(h):
        for j in xrange(w):
            
            flow = '-'
            mb = -1
            if i > 0 and m[i-1][j] < m[i][j] and m[i-1][j] < mb :
                flow = 'N'
                mb = m[i-1][j]
            if j > 0 and m[i][j-1] < m[i][j] and m[i][j-1] < mb:
                flow = 'W'
                mb = m[i][j-1]
            if i < h-2 and m[i+1][j] < m[i][j] and m[i+1][j] < mb:
                flow = 'E'
                mb = m[i+1][j]
            if j < h-2 and m[i][j+1] > m[i][j] and m[i][j+1] < mb:
                flow = 'S'
                mb = m[i][j+1]
            
            if flow == '-':
                cb += 1
                if i > 0:
                    bm[i-1][j] = cb
                if j > 0:
                    bm[i][j-1] = cb
                if i < h-2:
                    bm[i+1][j] = cb
                if j < w-2:
                    bm[i][j+1] = cb
                
            elif flow == 'N':
                bm[i-1][j] = cb
            elif flow == 'W':
                bm[i][j-1] = cb
            elif flow == 'E':
                bm[i+1][j] = cb
            elif flow == 'S':
                bm[i][j+1] = cb
    
    print bm
                  
    
    #s = "Case #%d:" % (i+1)
    #print s
    #o.write(s)

f.close()
o.close()