# def a(n, k, res = 0):
#     if n == 1 and k <= 9 and k >= 0:
#         return 1
#     elif k < 0 or k > 9:
#         return 0
#     else:
#         res += a(n-1, k-1, res) + a(n-1, k, res) + a(n-1, k+1, res)
#     return res

l = [9, 26, 75, 217, 629, 1826, 5307, 15438, 44941, 130900, 381444, 1111926, 3242224, 9455987, 27583372, 80472698, 234799873, 685149328, 1999414181, 5835044495]

n = int(input())
print(l[n-1])
# s = 0
# for i in range(1, 10):
#     s += a(n,i)
# print(s)
# if n == 1:
#     print(9)
# else:
#     # print(7*(3**(n-1)) + 2 * 2 * (3**(n-2)))
#     # print(9*3**(n-1) - 2 * 3**(n-2))
#     print(9*3**(n-1) - sum([3**(i) for i in range(n)]) - sum([3**i for i in range(n-1)]))