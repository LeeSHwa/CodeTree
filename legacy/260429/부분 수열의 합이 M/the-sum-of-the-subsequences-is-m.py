n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [float('inf')] * (m + 1)

# 초기상태 정의
dp[0] = 0

for num in nums:
    
    for idx in range(m, num - 1, -1):
        if dp[idx - num] != float('inf'):
            dp[idx] = min(dp[idx], dp[idx - num] + 1)

print(dp[-1] if dp[-1] != float('inf') else -1)