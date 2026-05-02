command = list(input())

x, y = 0, 0

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

dir = 0

for comm in command:
    if comm == "L":
        dir = (dir - 1) % 4
    elif comm == "R":
        dir = (dir + 1) % 4
    else:
        x += dx[dir]
        y += dy[dir]

print(x, y)
