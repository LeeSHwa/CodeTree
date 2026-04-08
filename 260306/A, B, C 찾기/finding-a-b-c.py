nums = list(map(int, input().split()))

nums.sort()

A = nums[0]
B = nums[1]

C = nums[-1] - B - A

print(A, B, C)

