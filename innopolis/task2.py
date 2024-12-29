n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

if b.count(0) < 2:
    if n == 2:
        print(min(a[0], b[1]) + min(a[1], b[0]))
    else:
        z = a.count(0)
        a1 = [int(i) for i in a if i != 0]
        ma = min(a1)
        mb = min(b)
        indb = b.index(mb)
        b.remove(mb)
        ab = a[indb]
        if ab > min(b):
            if sum(a) - ab > mb:
                print(max(mb + ab-min(b), ma + (n - 1 - z)))
            else:
                print(max(sum(a)-min(b), ma + (n - 1 - z)))
        else:
            # print(max(mb + ab, ma + (n - 1 - z)))
            if sum(a) - ab > mb:
                print(min(mb + ab, ma + (n - 1 - z)))
            else:
                print(min(sum(a), ma + (n - 1 - z)))
else: 
    print(0)