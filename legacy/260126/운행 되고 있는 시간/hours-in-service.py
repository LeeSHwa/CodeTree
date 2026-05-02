n = int(input())

devs = [tuple(map(int, input().split())) for _ in range(n)]

max_hour = -1

for i in range(n):
    
    curr_time = [False] * 1001

    for j in range(n):
        if j == i:
            continue

        start, end = devs[j]

        for k in range(start, end):
            curr_time[k] = True
        
    temp = curr_time.count(True)

    max_hour = max(max_hour, temp)

print(max_hour)
            
