k = int(input()) * 2
values = []
times = set()
points = 0
for _ in range(4):
    m = input()
    for i in m:
        if i != ".":
            values.append(int(i))
            times.add(int(i))
for i in times:
    if values.count(i) <= k:
        points += 1
print(points)