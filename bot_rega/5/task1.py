x = int(input())
ans = 0
lst = []
s = 1
c = s + x
while s <= c**0.7:
    
    if s % 2 == 0:
        n = s // 2
        m = (x + s - n)/(2*n + 1)
        if m < n:
            break
    else:
        
        m = (s + 1) // 2
        n = (x + s - m)/(2*m + 1)
        if n < m:
            break
    if (n + m).is_integer():
        ans += 1
        lst.append([int(n), int(m)])
    s += 1
    c = s + x

print(ans)
for i in lst:
    print(' '.join([str(l) for l in i]))
