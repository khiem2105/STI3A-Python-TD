def palindrome(s):
    return [s[i] for i in range(len(s))] == [s[len(s)-i-1] for i in range(len(s))]

# print(palindrome("abcba"))
assert palindrome("abba")
assert palindrome("abcba")
assert palindrome("")
assert palindrome("a")
assert not palindrome("ab")

def inverse(s):
    return [s[len(s)-i-1] for i in range(len(s))]

# print(inverse("abc"))
assert inverse("abc") == ["c", "b", "a"]
assert inverse("") == []

def palinv(s):
    return [c for c in s] == inverse(s)

assert palinv("abba")
assert palinv("abcba")
assert palinv("")
assert palinv("a")
assert not palinv("ab")

def rmfrom(s, bad):
    return [c for c in s if c not in bad]

# print(rmfrom("esope reste ici et se repose", "aeiouy "))

def rmspaces(s):
    return [c for c in s if c != " "]

# print(rmspaces("esope reste ici et se repose"))

def palindrome_sentence(s):
    return [s[i] for i in range(len(s)) if s[i] != " "] == [s[len(s)-i-1] for i in range(len(s)) if s[len(s)-i-1] != " "]

assert palindrome_sentence("esope reste ici et se repose")

def fsum(f, i, j):
    return sum(f(i) for i in range(i, j+1))

assert fsum(lambda i: i, 0, 10) == 55
assert fsum(lambda i: i*i, 0, 10) == 385

def isprime(n):
    return [i for i in range(1,int(n/2)+1) if n%i == 0] == [1]

assert isprime(31)

def comp(n):
    return {i for i in range(2, n+1) if not isprime(i)}

# print(comp(10))

def comp2(n):
    return {i for i in range(2, n+1) for j in range(2, i) if i%j == 0}
# print(comp2(10))

def comp3(n):
    return {i * j for i in range(2, int(n/2)) for j in range(2, int(n/i)+1)}

assert comp(100) == comp2(100) == comp3(100)
# print(comp3(100))

def primes(n):
    return tuple(i for i in range(2,n+1) if i not in comp(n))

assert primes(100) == tuple(k for k in range(2, 100+1) if isprime(k))    

def crange(a, b):
    return (chr(c) for c in range(ord(a), ord(b)+1))

# gen = crange("a", "z")
# print(next(gen))
# print(next(gen))
# print(next(gen)) 

assert "".join(crange("A", "Z")) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def charrange(*args):
    if args != ():
        i = 0
        while i < len(args):
            yield from crange(args[i], args[i+1])
            i += 2
    return ""

# gen = charrange("A", "Z", "a", "z", "0", "9")
# print(next(gen))
# print(next(gen))
# print(next(gen))

assert "".join(charrange("A", "Z", "a", "z", "0", "9")) ==\
         "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
assert "".join(charrange()) == ""                    

