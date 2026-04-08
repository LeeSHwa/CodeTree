from collections import defaultdict
# white = [0], black = [1], last color = [2]
N = int(input())

tiles = defaultdict(list)
pos = 0

for _ in range(N):
    distance, direction = input().split()
    distance = int(distance)

    if direction == "R":
        for i in range(pos, pos + distance):
            if tiles[i]:
                tiles[i][1] += 1
            else:
                tiles[i] = [0, 0, -1]
                tiles[i][1] = 1

            tiles[i][2] = 1

        pos = pos + distance - 1
    
    else:
        for i in range(pos - distance + 1, pos + 1):
            if tiles[i]:
                tiles[i][0] += 1
            else:
                tiles[i] = [0, 0, -1]
                tiles[i][0] = 1


            tiles[i][2] = 0

        pos = pos - distance + 1
        

count = [0] * 3

for white, black, last in tiles.values():
    if white >= 2 and black >= 2:
        count[2] += 1
    elif last == 1:
        count[1] += 1
    else:
        count[0] += 1

print(" ".join(map(str, count)))