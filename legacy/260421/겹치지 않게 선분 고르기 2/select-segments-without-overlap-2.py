n = int(input())

MAX_RANGE = 1001

dp = [0] * MAX_RANGE

# pos = [tuple(map(int, input().split())) for _ in range(n)]
# pos.sort(key = lambda x : x[1])

line = {}

for _ in range(n):
    x1, x2 = map(int, input().split())

    if x1 in line:
        line[x1] = min(line[x1], x2)
    else:
        line[x1] = x2

pos = sorted(line.items(), key = lambda x : x[1])

for x1, x2 in pos:
    
    max_value = -1
    for end in range(x1):
        max_value = max(max_value, dp[end])
    
    dp[x2] = max(dp[x2], max_value + 1)

print(max(dp))
    