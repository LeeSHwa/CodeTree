N = int(input())

nums = [int(input()) for _ in range(N)]

# print(nums)

max_value = -1
def is_carry(a, b, c):
    while a or b or c:
        if (a % 10) + (b % 10) + (c % 10) >= 10:
            return True
        else:
            a //= 10
            b //= 10
            c //= 10
    
for i in range(N-2):
    for j in range(i + 1, N-1):
        for k in range(j + 1, N):
            if not is_carry(nums[i], nums[j], nums[k]):
                max_value = max(max_value, nums[i] + nums[j] + nums[k])

print(max_value)
                