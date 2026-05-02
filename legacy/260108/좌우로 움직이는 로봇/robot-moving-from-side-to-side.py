N, M = map(int, input().split())

def solve(N):    
    hour = 0
    move = []
    log = []

    for i in range(N):
               
        time, dirs = input().split()
        time = int(time)
        dirs = 1 if dirs == "R" else -1

        for _ in range(time):
            if hour == 0:
                log = [dirs]
                hour = 1
            else:    
                log.append(log[hour - 1] + dirs)
                hour += 1

    return log

A_log = solve(N)
B_log = solve(M)

bigger_log_length = max(len(A_log), len(B_log))

if len(A_log) < bigger_log_length:
    extra = A_log[-1]
    for _ in range(bigger_log_length - len(A_log)):
        A_log.append(extra)

if len(B_log) < bigger_log_length:
    extra = B_log[-1]
    for _ in range(bigger_log_length - len(B_log)):
        B_log.append(extra)

count = 0
for i in range(1, bigger_log_length):
    if A_log[i-1] != B_log[i-1] and A_log[i] == B_log[i]:
        count += 1

print(count)