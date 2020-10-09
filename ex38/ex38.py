def upto(g, i):
    return (next(g) for _ in range(i))

assert list(upto((x for x in range(3)), 8)) == [0, 1, 2]
assert list(upto((n*n for n in range(100)), 7)) == \
        [0, 1, 4, 9, 16, 25, 36]

def nth(g, n):
    return [next(g) for _ in range(n+1)][n]

assert all(nth(g, i) == i*i for i in range(7) for g in [(n*n for n in range(7))])

def power(f, s):
    n = 0
    g = power(f, s)
    while True:
        if n == 0:
            yield(s)
        else:    
            yield f(next(g))
        n += 1    

gen = power(lambda x:2*x, 1)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(list(next(gen) for _ in range(7)))

assert list(upto(power(lambda x:2*x, 1), 7)) == \
        [1, 2, 4, 8, 16, 32, 64]

def group(l):
    i = 0
    while i < len(l):
        grp = []
        grp.append(l[i])
        if i < len(l) - 1:
            j = i+1
            while j < len(l) and l[j] == l[i]:
                grp.append(l[j])
                j += 1
            i = j
        else:
            i += 1    
        yield grp

# print(list(group("aaba")))        

assert list(group("")) == []
assert list(group("a")) == [["a"]]
assert list(group("aaba")) == [["a", "a"], ["b"], ["a"]]
assert list(group("aabbbcdaaaa")) == \
    [["a", "a"], ["b", "b", "b"], ["c"], ["d"], ["a", "a", "a", "a"]]

def groupn(l):
    i = 0
    while i < len(l):
        n = 1
        if i < len(l) - 1:
            j = i+1
            while j < len(l) and l[j] == l[i]:
                n += 1
                j += 1
            i = j
        else:
            i += 1
        yield n, l[i-1]    

assert list(groupn("aabbbcdaaaa")) == \
        [(2, "a"), (3, "b"), (1, "c"), (1, "d"), (4, "a")]

def groupl(g):
    pass

def say(s):
    l = list(groupn(s))
    new_str = str()
    for tup in l:
        new_str = new_str + str(tup[0]) + tup[1]
    return new_str

# print(list(upto(power(say, "22"), 7)))

def conway(seed="1", maxrnk=100, maxlen=10):
    gen = upto(power(say, "1"), 20)
    for i in range(maxrnk+1):
        print(f"{i:>3} {next(gen):5}")

conway()
