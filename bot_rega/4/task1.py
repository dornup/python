import sys
sys.setrecursionlimit(100000)

def a(n, k, lst):
    if k == 1:
        lst.append(n[:2])
        return n[:2], lst
    else:
        p = n[:2]
        lst.append(p)
        p1 = p.copy()
        winner = max(p1)
        p1.remove(winner)
        loser = p1[0]
        n = [winner] + n[2:] + [loser]
        return a(n, k-1, lst)


N = int(input())
que = list(map(int, input().split()))
Q = int(input())
lst1 = []

for i in range(Q):
    k = int(input())
    if k < len(lst1):
        print(" ".join([str(i) for i in lst1[k-1]]))
    else:
        ans, lst1 = a(que, k, [])
        print(" ".join([str(i) for i in ans]))

    