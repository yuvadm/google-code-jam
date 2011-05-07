f = open('3.in', 'r')
o = open('3.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    line = f.readline().strip().split(' ')
    
    C = int(line[0])
    comb = line[1:1+C]
    D = int(line[C+1])
    opp = line[C+2:C+2+D]
    s = [x for x in line[-1]]
    
    cd = dict([(x[0:2], x[2]) for x in comb])
    od = opp
    
    el = []
    print cd, od, s
    for c in s:
        
        if not el:
            el.append(c)
            continue
        
        last = el[-1]
        lc = last + c
        cl = c + last
        
        if cd.get(lc):
            el.pop()
            el.append(cd.get(lc))
        elif cd.get(cl):
            el.pop()
            el.append(cd.get(cl))
        elif any([c + e in od or e + c in od for e in el]):
            el = []
        else:
            el.append(c)            
            
    res = '[' + ', '.join(el) + ']'
    s = "Case #%d: %s\n" % (t+1, res)
    o.write(s)

f.close()
o.close()