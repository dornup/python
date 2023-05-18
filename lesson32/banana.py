a = input().split(" ")
k, n, w = int(a[0]), int(a[1]), int(a[2])
stoim = 0

for i in range(w):
    c = k * (i+1)
    stoim += c

dolg = stoim - n
if dolg < 0:
    print(0)
else:
    print(dolg)
