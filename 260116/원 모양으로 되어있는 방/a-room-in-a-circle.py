N = int(input())
circle = [int(input()) for _ in range(N)]

min_distance = float('inf')

for start in range(N):
    temp = circle[start + 1:]
    temp.extend(circle[:start])

    curr_distance = 0
    # print(*temp)
    for idx, value in enumerate(temp, 1):
        # print(f"start : {start}, idx : {idx}, value : {value}")
        curr_distance += idx * value

    # print(curr_distance)

    min_distance = min(min_distance, curr_distance)    
    
print(min_distance)