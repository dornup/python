t = int(input())
ans = []
for i in range(t):
    n, k = nums = input().split(' ')
    ans.append(int(n) * int(k))

for i in ans:
    print(i)