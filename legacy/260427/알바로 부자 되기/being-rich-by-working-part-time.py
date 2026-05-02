n = int(input())

works = [list(map(int, input().split())) for _ in range(n)]


dp = [0] * n
dp[0] = works[0][2]

for i in range(1, n):
    
    for j in range(i):
        if works[i][0] > works[j][1]:
            dp[i] = max(dp[i], dp[j] + works[i][2])

        if works[i][2] > dp[i]:
            dp[i] = works[i][2]

print(max(dp))