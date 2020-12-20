import timeit


s1 = """
a = {}
b = [1,1,1,1,1]
c = ['a','a','a','a','a']

for i in range(1000):
    b[0] = i
    d = tuple(b + c)
    a[d] = i

b[0] = 1000
"""
c1 = """
d = tuple(b + c)
if d in a:
    pass
"""
s2 = """
a = {}
b = [1,1,1,1,1]
c = [-1,-1,-1,-1,-1]

for i in range(1000):
    b[0] = i
    d = tuple(b + c)
    a[d] = i

b[0] = 1000
"""
c2 = """
d = tuple(b + c)
if d in a:
    pass
"""


print(timeit.timeit(c1, s1, number=1000000))
print(timeit.timeit(c2, s2, number=1000000))
