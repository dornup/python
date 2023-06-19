m = input().split()
s = int(input())
for _ in range(s):
        m.insert(0, m[-1])
        m.pop(-1)
print(" ".join(m))
