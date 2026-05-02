n, m = map(int, input().split())

nums = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True

for num in nums:

    for idx in range(m, num - 1, -1):
        if idx >= num and dp[idx - num]:
            dp[idx] = True
    
print("Yes" if dp[m] != False else "No")