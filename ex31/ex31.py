import math
# from gplot import *
from timeit import *

def issqrt_builtin(n):
    return math.floor(math.sqrt(n))

assert [issqrt_builtin(n) for n in range(30)] ==\
        [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]

def issqrt_hard(n):
    i = 0
    while i*i <= n:
        i += 1
    return i - 1

for n in range(100):
    assert issqrt_hard(n) == issqrt_builtin(n)

def issqrt_sum(n):
    i = 1
    sum = 0
    while sum <= n:
        sum += 2*i - 1
        i += 1
    return i - 2   
# print([issqrt_sum(n) for n in range(30)])
for n in range(100):
    assert issqrt_sum(n) == issqrt_builtin(n)

def issqrt_dicho(n):
    if n == 0:
        return 0
    l = 0
    r = n - 1
    while l <= r:
        m = math.floor((l + r)/2)
        if m*m == n:
            return m
        elif m*m < n:
            if (m+1)*(m+1) == n:
                return m+1
            if (m+1)*(m+1) > n:
                return m
            l = m + 1    
        elif m*m > n:
            if (m-1)*(m-1) <= n:
                return m - 1
            r = m - 1
# print([issqrt_dicho(n) for n in range(30)])
for n in range(100):
    assert issqrt_dicho(n) == issqrt_builtin(n)

timeit(stmt='issqrt_hard(1000)', setup="from __main__ import issqrt_hard")
timeit.Timer(issqrt_hard(1000)).timeit(number=1000)
