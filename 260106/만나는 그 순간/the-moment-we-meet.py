N, M = map(int, input().split())
A_log = [0] * (2000001)
B_log = [0] * (2000001)

pos = 0
time = 0
A_total_distance = 0
for i in range(N):
    dirs, distance = input().split()
    distance = int(distance)

    if dirs == "R":
        for _ in range(distance):
            time += 1
            pos += 1
            A_log[time] = pos
    
    else:
        for _ in range(distance):
            time += 1
            pos -= 1
            A_log[time] = pos

    A_total_distance += distance

pos = 0
time = 0

B_total_distance = 0
for i in range(M):
    dirs, distance = input().split()
    distance = int(distance)

    if dirs == "R":
        for _ in range(distance):
            time += 1
            pos += 1
            B_log[time] = pos
    
    else:
        for _ in range(distance):
            time += 1
            pos -= 1
            B_log[time] = pos
    
    B_total_distance += distance

end = min(A_total_distance, B_total_distance)

for index in range(1, end):
    if A_log[index] == B_log[index]:
        print(index)
        exit()

print(-1)