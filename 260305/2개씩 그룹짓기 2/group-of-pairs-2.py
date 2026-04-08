n  = int(input())

nums = list(map(int, input().split()))
nums.sort()

min_diff = float('inf')
for i in range(n):
    min_diff = min(min_diff, nums[n+i] - nums[i])

print(min_diff)