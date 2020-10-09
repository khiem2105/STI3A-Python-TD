def data(m):
    i = 1
    while i <= m:
        print (f"Data yields 0; has {m-i} left")
        yield 0
        i+= 1
    print ("Data is exhausted ")

def chaingens (g,lvl):
    while True:
        print (f"lvl {lvl} gen asks")
        d = next(g)
        res = d + 1
        print (f"lvl {lvl} gen obtains {d}, yields {res}")
        yield res

def genchain (n,m):
    if n == 0:
        return data(m)
    else:
        return chaingens ( genchain (n-1,m),n)

g = genchain (3,3)
for v in g:
    print (f" Final computation depth : {v}\n")