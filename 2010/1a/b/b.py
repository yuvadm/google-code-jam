f = open('1.in', 'r')
o = open('1.out', 'w')

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
def smooth(a, f, d, i, m):
    if not a:
        return 0

    best = smooth(a[:-1], f, d, i, m) + d

T = int(f.readline().strip())

for t in range(T):
    (d, i, m, _n) = map(int, f.readline().strip().split(' '))
    A = map(int, f.readline().strip().split(' '))
    r = smooth(A, d, i, m)
    s = "Case #%d: %s\n" % (t+1, r)
    print s
    o.write(s)
