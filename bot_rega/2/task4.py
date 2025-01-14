n, k = map(int, input().split())
num = map(int, input().split())
num = sorted(num)
mid = n//2
for i in range(k):
    num[mid] += 1
    num = sorted(num)

print(num[mid])