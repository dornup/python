f = open("input.txt")
w = open("output.txt", 'w')
l = [i.rstrip('\n') for i in f.readlines()]
nums = [int(i) for i in l[-1].split(' ')]
user = 1
sum_user_1 = 0
sum_user_2 = 0
for i in range(int(l.pop(0))):
    n1, n2 = nums[0], nums[-1]
    if len(nums) > 2:
        if nums[-2] - nums[1] > nums[-1] - nums[0]:
            exec(f'sum_user_{user} += nums[0]')
            nums.remove(nums[0])
        elif nums[1] - nums[-2] > nums[0] - nums[-1]:
            exec(f'sum_user_{user} += nums[-1]')
            nums.remove(nums[-1])
        else:
            exec(f'sum_user_{user} += max(n1, n2)')
            nums.remove(max(n1, n2))
    else:
        exec(f'sum_user_{user} += max(n1, n2)')
        nums.remove(max(n1, n2))

    if user == 1:
        user = 2
    else:
        user = 1
if sum_user_1 > sum_user_2:
    w.write('1')
elif sum_user_2 > sum_user_1:
    w.write('2')
else:
    w.write('0')
f.close()
w.close()

