N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

UNUSED = -float('inf')
dp = [UNUSED] * (M + 1)
dp[0] = 0


for weight in range(1, M + 1):
    
    for i in range(N):
        if weight >= w[i]:
            dp[weight] = max(dp[weight], dp[weight - w[i]] + v[i])

print(max(dp))