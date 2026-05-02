n = int(input())

nums = [int(input()) for _ in range(n)]

avg = sum(nums) // n

ans = 0
for num in nums:
    if num > avg:
        ans += num - avg

print(ans)