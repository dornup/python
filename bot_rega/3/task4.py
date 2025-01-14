n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
    t, i, x = map(int, input().split())
    if t == 0:
        a[i-1] = x
    else:
        b = i
        while a[b-1] < x and b < n + 1:
            b += 1
        print(a)