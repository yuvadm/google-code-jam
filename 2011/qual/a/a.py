f = open('3.in', 'r')
o = open('3.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    line = f.readline().strip().split(' ')[1:]
    prs = zip(line[::2], map(int,line[1::2]))
    
    oprs = [x[1] for x in prs if x[0]=='O']
    bprs = [x[1] for x in prs if x[0]=='B']
    
    op, bp = 1, 1
    
    step = 0
    while (prs):
        step += 1
        #print prs, oprs, bprs, op, bp
        pushed = False
        if oprs:
            if prs[0] == ('O', op):
                oprs = oprs[1:]
                prs = prs[1:]
                pushed = True
            elif oprs[0] > op:
                op += 1
            elif oprs[0] < op:
                op -= 1
                
        if bprs:
            if prs[0] == ('B', bp) and not pushed:
                bprs = bprs[1:]
                prs = prs[1:]
            elif bprs[0] > bp:
                bp += 1
            elif bprs[0] < bp:
                bp -= 1
    
    res = step
    s = "Case #%d: %d\n" % (t+1, res)
    #print s
    o.write(s)

f.close()
o.close()