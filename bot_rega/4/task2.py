# def fib(buildings, k):
#     if k == 0:
#         return sum(buildings)
#     else:
#         return fib([sum(buildings[:i+1]) for i, e in enumerate(buildings)], k - 1)


N, K, R = map(int, input().split())
obj = list(map(int, input().split()))

k_table = [[1 for i in range(N)]]
for i in range(K-1):
    k_table.append([0 for i in range(N)])

for i in range(1, K):
    for j in range(N):
        if j == 0:
            k_table[i][j] = k_table[i-1][j]
        else:
            k_table[i][j] = k_table[i-1][j] + k_table[i][j-1]

for i in reversed(k_table):
    f = False
    a = 1
    for j in range(N-1, 0, -1):
        a = max(i[:j+1])
        # print(i[:j+1])
        if R % a == 0:
            f = True
            break
    if f:
        break

# print(k_table)
print(R//a)


# print(fib(obj, K))
# n, k, r = map(int, input().split())
# obj = list(map(int, input().split()))
# lst = []
# listik = [].append(obj)
# for i in range(k):
#     obj[i] = sum(obj[:i+1])
#     listik.append(obj)