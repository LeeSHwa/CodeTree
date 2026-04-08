n = int(input())
nums = sorted(list(map(int, input().split())))
max_num = -float('inf')

# 1. 길이가 3일 경우
if len(nums) == 3:
    max_num = max(max_num, nums[0] * nums[1] * nums[2])

# 2. 음, 음, 양
max_num = max(max_num, nums[0] * nums[1] * nums[-1])

# 3. 양, 양, 양
max_num = max(max_num, nums[-1] * nums[-2] * nums[-3])

# 4. 0이 있다면
if 0 in nums:
    max_num = max(max_num, 0)

print(max_num)