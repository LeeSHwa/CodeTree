n = int(input())

seats = list(input())

distance = [float('inf')] * n

# left
curr = float('inf')
for i in range(n):
    if seats[i] == '1':
        curr = 0
    else:
        curr += 1
    
    distance[i] = min(distance[i], curr)

# right
curr = float('inf')
for i in range(n-1, -1, -1):
    if seats[i] == '1':
        curr = 0
    else:
        curr += 1
    
    distance[i] = min(distance[i], curr)

candidate = distance.index(max(distance))

seats[candidate] = '1'

last = seats.index('1')
min_distance = float('inf')
for i in range(last + 1, n):
    curr_distance = 0
    if seats[i] == '1':
        curr_distance = i - last
        last = i
    
        min_distance = min(min_distance, curr_distance)

print(min_distance)