command = list(input())

x, y = 0, 0

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

dir = 0
total_time = 0

for comm in command:
    total_time += 1
    
    if comm == "L":
        dir = (dir - 1) % 4
    elif comm == "R":
        dir = (dir + 1) % 4
    else:
        x += dx[dir]
        y += dy[dir]
        
        if x == 0 and y == 0:
            print(total_time)
            exit()

    
print(-1)
