s = input().split()
ch = int(input())
m = set()
for i in s:
    for k in s:
        if int(i) + int(k) == ch:
            m.add(int(i))
            m.add(int(k))
print(m)
