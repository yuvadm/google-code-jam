import re

f = open('3.in', 'r')
o = open('3.out', 'w')

ldn = f.readline().strip().split(' ')
l = int(ldn[0])
d = int(ldn[1])
n = int(ldn[2])

dicts = '\n'.join([f.readline().strip() for i in xrange(d)])

for i in xrange(n):
    exp = f.readline().strip()
    exp = exp.replace('(','[').replace(')',']')
    
    r = len(re.findall(exp, dicts))
    
    s = "Case #%d: %s\n" % (i+1, r)
    o.write(s)

f.close()
o.close()