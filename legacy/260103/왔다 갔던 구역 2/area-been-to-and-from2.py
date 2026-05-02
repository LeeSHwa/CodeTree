pos = 0
line = [0] * 2002
offset = 1000

pos += offset

N = int(input())

for _ in range(N):
    distance, direction = input().split()
    distance = int(distance)

    if direction == "L":
        for i in range(pos - distance, pos):
            line[i] += 1
        pos -= distance
            
    else:
        for i in range(pos, pos + distance):
            line[i] += 1
        pos += distance
        
count = 0
for i in line:
    if i >= 2:
        count += 1

print(count)