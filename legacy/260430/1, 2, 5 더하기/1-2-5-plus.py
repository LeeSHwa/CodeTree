n = int(input())

MOD = 10007

dp = [float('inf')] * (n + 6)

# 초기상태 정의
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 9


for i in range(6, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 5]) % MOD

print(dp[n])