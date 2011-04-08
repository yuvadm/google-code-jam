class memoized(object):
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         return self.func(*args)

@memoized
def countSub(sub, s):
    (lsub, ls) = (len(sub), len(s))
    
    if lsub == ls:
        return 1 if sub == s else 0
        
    if lsub > ls:
        return 0
        
    if lsub == 0:
        return 1

    if ls == 0:
        return 0
    
    if sub[0] == s[0]:
        return isSub(sub[1:], s[1:])
    else:
        return isSub(sub, s[1:])

f = open('1.in', 'r')
o = open('1.out', 'w')

t = int(f.readline().strip())

WTCJ = 'welcome to code jam'

for i in xrange(t):
    sub = f.readline().strip()
    
    prefs = [sub[j:] for j in xrange(len(sub))]
    print prefs
    
    r = len(filter(lambda x: isSub(WTCJ, x), prefs))
    
    s = "Case #%d: %d" % (i+1, r)
    print s
    o.write(s)

f.close()
o.close()