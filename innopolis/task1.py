from math import ceil
n, x = int(input()), int(input())
pow_2 = 2**x
res = 0
if n > 1:
    start = 10**(n-1)
else:
    start = 0
    res += 1
if pow_2 < 10**n:
    if pow_2 < 10**(n-1):
        for i in range(start, 10**n, 2):
            if not i % pow_2:
                first = i
                break
    else:
        first = pow_2
    res += int(ceil((10**n-first)/pow_2))
    print(res)
else:
    print(1 if start == 0 else 0)
