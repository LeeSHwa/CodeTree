nums = list(map(int, input().split()))
nums.sort()

if nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1:
    print(0)
elif nums[1] - nums[0] == 2 or nums[2] - nums[1] == 2:
    print(1)
else:
    print(2)
