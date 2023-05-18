a = input().split(" ")
c = 0
a, b = int(a[0]), int(a[1])
while a <= b:
    a *= 3
    b *= 2
    c += 1
print(c)