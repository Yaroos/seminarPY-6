a1 = int(input('a1: '))
n = int(input('n: '))
d = int(input('d: '))
last = a1 + (n-1) * d
res = [x for x in range(a1, last+1, d)]
print(*res)
