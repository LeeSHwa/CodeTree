n, m = map(int, input().split())

coins = list(map(int, input().split()))

dp = [-float('inf')] * (m + 1)

dp[0] = 0

for idx in range(1, m + 1):
    for coin in coins:
        if idx >= coin:
            dp[idx] = max(dp[idx], dp[idx - coin] + 1)

print(dp[-1] if dp[-1] != -float('inf') else -1)