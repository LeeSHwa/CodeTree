N, M, p = map(int, input().split())
timeline = {}

programmers = set([chr(x) for x in range(65, 65 + N)])


for time in range(M):
    timeline[time] = input().split()

    if time >= (p - 1) and timeline[time][0] in programmers:
        programmers.discard(timeline[time][0])

temp = timeline[p - 1][1]

if timeline[p - 1][1] == '0':
    exit()

for time in range(p - 1):
    if timeline[time][1] == temp:
        programmers.discard(timeline[time][0])

print(*programmers)