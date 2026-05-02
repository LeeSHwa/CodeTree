N = int(input())
seats = list(map(int, input()))

MAX_DISTANCE = 20

distance = [MAX_DISTANCE] * N 

cnt = MAX_DISTANCE
# LEFT
for i in range(N):

    if seats[i] == 1:
        cnt = 0
    else:
        cnt += 1

    distance[i] = cnt

cnt = MAX_DISTANCE
# RIGHT
for i in range(N - 1, -1, -1):

    if seats[i] == 1:
        cnt = 0
    else:
        cnt += 1

    distance[i] = min(distance[i], cnt)

max_distance = max(distance)

candidates = [idx for idx, d in enumerate(distance) if d == max_distance]

ans = float('inf')

for idx in candidates:
    seats[idx] = 1
    
    curr_distance = float('inf')
    last_person = -1

    for i in range(N):
        if seats[i] == 1:
            if last_person != -1:
                curr_distance = min(curr_distance, i - last_person)
            last_person = i


    ans = min(ans, curr_distance)

    seats[idx] = 0

print(ans)
    