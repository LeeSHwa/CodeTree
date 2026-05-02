# white = [0], black = [1]
N = int(input())

tiles = {}
pos = 0

for _ in range(N):
    distance, direction = input().split()
    distance = int(distance)

    if direction == "R":
        for i in range(pos, pos + distance):
            tiles[i] = 1

        pos = pos + distance - 1
    
    else:
        for i in range(pos - distance + 1, pos + 1):
            tiles[i] = 0
            
        pos = pos - distance + 1
        

count = [0] * 2

for color in tiles.values():
    if color:
        count[1] += 1
    else:
        count[0] += 1

print(" ".join(map(str, count)))