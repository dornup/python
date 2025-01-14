import math
n, x, y = map(int, input().split())
copies = 1
time = min(x,y)
cur_x, cur_y = x, y
t1 = math.lcm(x,y)
d = {}
copies1 = 0

for i in range(1, t1 + 1):
    cur_x -= 1
    cur_y -= 1
    if cur_x == 0:
        copies1 += 1
        cur_x = x
        d[copies1] = i
    if cur_y == 0:
        copies1 += 1
        cur_y = y
        d[copies1] = i

time += t1 * (n // copies1)
copies += copies1 * (n // copies1)
time += d[n - copies] if n - copies > 0 else 0 


print(time)