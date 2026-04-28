def solve():
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))

    if min(coins) > m:
        return -1

    dp = [float('inf')] * (m + 1)

    for coin in coins:
        if m > coin:
            dp[coin] = 1

    for i in range(1, m + 1):

        for coin in coins:
            if i - coin > 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    
    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]

ans = solve()

print(ans)