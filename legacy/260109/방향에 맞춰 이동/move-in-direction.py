from enum import Enum
class Directions(Enum):
    N = 0
    S = 1
    E = 2
    W = 3

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # N, S, E, W

x, y = 0, 0

N = int(input())

for _ in range(N):
    dir, distance = input().split()
    distance = int(distance)

    idx = Directions[dir].value

    dx, dy = dirs[idx]

    x += dx * distance
    y += dy * distance


print(x, y)