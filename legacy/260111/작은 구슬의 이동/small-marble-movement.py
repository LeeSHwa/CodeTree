N, T = map(int, input().split()) # N x N / T초 후

R, C, D = input().split() # (R, C), dirs

dr = [-1, 0,  0, 1]
dc = [ 0, 1, -1, 0]
    #  D, R,  L, U
# (3 - dir) % 4
# dir 1 : 2
# dir 3 : 0
# dir 0 : 3 
# dir 2 : 1 
dirs = {"U" : 0, "R" : 1, "L" : 2, "D" : 3}
dir = dirs[D]

pos_r = int(R)
pos_c = int(C)

for _ in range(T):
    if pos_r + dr[dir] < 1 or pos_r + dr[dir] > N or pos_c + dc[dir] < 1 or pos_c + dc[dir] > N:
        dir = (3 - dir) % 4
    
    else: 
        pos_r += dr[dir]
        pos_c += dc[dir]

print(pos_r, pos_c)