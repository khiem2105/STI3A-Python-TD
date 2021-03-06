import math as m 

def greatest_root(a, b, c):
    assert a != 0
    if b*b - 4*a*c >= 0:
        if a > 0 or b < 0:
            return (-b + m.sqrt(b*b - 4*a*c))/2*a
        else:
            return (-b - m.sqrt(b*b - 4*a*c))/2*a
    return None

def real_roots(a, b, c):
    assert a != 0
    if b*b - 4*a*c >= 0:
        return ((-b + m.sqrt(b*b - 4*a*c))/2*a, (-b - m.sqrt(b*b - 4*a*c))/2*a)
    return ()

for a in range(-5, 5+1):
    if a != 0:
        continue
    for b in range(-5, 5+1):
        for c in range(-5, 5+1):
            if greatest_root(a, b, c) is not None:
                assert greatest_root(a, b, c) in real_roots(a, b, c)

__is = range(-5, 6)

assert all(max(real_roots(a, b, c)) == greatest_root(a, b, c)
            if real_roots(a, b, c) else greatest_root(a, b, c) is None
            for a in __is for b in __is for c in __is 
            if a != 0)
