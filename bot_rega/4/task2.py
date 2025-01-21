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

a = 1
a_max = 1
for i in reversed(k_table):
    f = False
    for j in range(N-1, 0, -1):
        a = max(i[:j+1])
        # print(i[:j+1])
        if R % a == 0:
            f = True
            a1 = a
            break
    if f:
        if a1 > a_max:
            a_max = a1
        
# print(a_max)

# print(k_table)
print(R//a_max)


# print(fib(obj, K))
# n, k, r = map(int, input().split())
# obj = list(map(int, input().split()))
# lst = []
# listik = [].append(obj)
# for i in range(k):
#     obj[i] = sum(obj[:i+1])
#     listik.append(obj)