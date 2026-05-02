def solve():
    n = int(input())

    nums = list(map(int, input().split()))

    if nums[0] == 0:
        return 0

    dp = [0] * n

    for i in range(1, n):
        
        dp[i] = 0

        for j in range(i):
            if j + nums[j] >= i:
                dp[i] = max(dp[i], dp[j] + 1)

        if dp[i] == 0:
            break

    # print(dp)
    return max(dp)

ans = solve()
print(ans)