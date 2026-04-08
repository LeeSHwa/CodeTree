N, M = map(int, input().split())

def solve(N):    
    hour = 0
    move = []
    log = []

    for i in range(N):
        move.append(list(map(int, input().split()))) # (v, t)
        
        time = move[i][1]
        velocity = move[i][0]

        for _ in range(time):    # t시간동안 v만큼 이동
            if hour == 0:
                log = [move[0][0]]
                hour = 1
            else:    
                log.append(log[hour - 1] + velocity)
                hour += 1

    return log

A_log = solve(N)
B_log = solve(M)

count = 0
honer = []
last_honer = []

for i in range(len(A_log)):
    if A_log[i] == B_log[i]:
        honer = [1, 2]
    elif A_log[i] > B_log[i]:
        honer = [1]
    else:
        honer = [2]

    if last_honer != honer:
        count += 1
    
    last_honer = honer
            
print(count)