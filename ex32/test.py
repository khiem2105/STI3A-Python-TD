def r(i,j):
    while i <= j:
        yield i
        i += 1

it = r(2,7)

print(next(it))
print(next(it))
