N, K = map(int, input().split())

positions = [0] * 101
min_pos = 101
max_pos = -1

for _ in range(N):
    candy, pos = map(int, input().split())
    
    positions[pos] += candy
    
    min_pos = min(min_pos, pos)
    max_pos = max(max_pos, pos)

max_value = -1

for pos in range(min_pos, max_pos + 1):
    
    start = 0 if pos - K < 0 else pos - K
    end = 100 if pos + K > 100 else pos + K
    # print(start, end)
    
    candies = positions[start : end + 1]
    max_value = max(max_value, sum(candies))

print(max_value)