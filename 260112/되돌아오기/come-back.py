N = int(input())

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_dict = {"N" : 0, "S" : 1, "E" : 2, "W" : 3}
x, y = 0, 0
time = 0

for _ in range(N):
    dirs, distance = input().split()
    distance = int(distance)
    dx, dy = direction[dir_dict[dirs]]

    for _ in range(distance):
        x, y = x + dx, y + dy
        time += 1
        
        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)
