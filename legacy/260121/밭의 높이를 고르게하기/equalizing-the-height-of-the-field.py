N, H, T = map(int, input().split()) # N개의 밭, H의 높이를 만족하는 밭이 최소 T개가 되도록

field = list(map(int, input().split()))
diff = []

for idx in range(N):
    diff.append(abs(field[idx] - H))

ans = float('inf')

for i in range(len(diff) - T + 1):
    curr_sum = sum(diff[i:i+T])
    ans = min(ans, curr_sum)

print(ans)