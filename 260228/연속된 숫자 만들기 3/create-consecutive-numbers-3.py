nums = list(map(int, input().split()))

max_distance = max(nums[1] - nums[0], nums[2] - nums[1])

print(max_distance - 1)