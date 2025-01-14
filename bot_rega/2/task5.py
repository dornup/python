def a(n, nums, x, res=0):
    if x < n-2:
        if a(n, nums, x+1) + nums[x+1] < a(n, nums, x+2) + nums[x+2]:
            res += a(n, nums, x+1, res) + nums[x+1]
        else:
           res += a(n, nums, x+2, res) + nums[x+2]
    elif x == n - 2:
        res += a(n, nums, x+1, res) + nums[x+1]
    else:
        return 0
    return res
        


n = int(input())
nums = list(map(int, input().split()))
x = 0
i = -1

print(a(n, nums, -1))

# while i < n-1:
#     if i < n-2:
#         f = nums[i+1]
#         s = nums[i+2]
#         if f < s:
#             x += f
#             i += 1
#         else:
#             x += s
#             i += 2
#     else:
#         x += nums[i+1]
#         i += 1

# print(x)