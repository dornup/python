from math import log
# rmq with sparse table
N = int(input())
lst = list(map(int, input().split()))
# Препроцессинг 
ST = []
k = int(log(N, 2))
for i in range(k + 1):
    line = []
    # print(ST)
    for l in range(N - 2**i + 1):
        if i == 0:
            line = lst
        else:
            # print(l, i)
            line.append(max(ST[i-1][l], ST[i-1][l + 2**(i-1)]))
    ST.append(line)

t = int(input())
a = []
for i in range(t):
    i, j = map(int, input().split())
    k = int(log(j - i + 1))
    a.append(max(ST[k][i-1], ST[k][j - 2**k]))

for i in range(t):
    print(a[i])
