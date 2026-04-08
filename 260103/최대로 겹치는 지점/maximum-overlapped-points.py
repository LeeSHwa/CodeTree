N = int(input())

line = [0] * 101

for _ in range(N):
    start, end = map(int, input().split())

    for i in range(start, end + 1):
        line[i] += 1

print(max(line))
    