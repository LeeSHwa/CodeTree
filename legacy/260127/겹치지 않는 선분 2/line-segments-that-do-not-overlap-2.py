n = int(input())

pos = [tuple(map(int, input().split())) for _ in range(n)]

pos.sort(key = lambda x : x[0])

L_MAX = [0] * n
R_MIN = [0] * n

temp = -float('inf')
for i in range(n):
    L_MAX[i] = temp
    temp = max(temp, pos[i][1])


temp = float('inf')
for i in range(n-1, -1, -1):
    R_MIN[i] = temp
    temp = min(temp, pos[i][1])


cnt = 0
for idx in range(n):
    if pos[idx][1] > L_MAX[idx] and pos[idx][1] < R_MIN[idx]: 
        cnt += 1

print(cnt)