def one(c, a):
    return [i&c for i in a]

def two(c, a):
    return [i|c for i in a]

def three(c, a):
    return [i^c for i in a]

def four(i, a):
    print(a[i-1])

def five(i, a):
    print(sorted(a)[i-1])

d = {
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five
}

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        func, c = input().split()
        if int(func) < 4:
            a = d[func](int(c), a)
        else:
            d[func](int(c), a)
