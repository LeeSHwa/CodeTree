# n, k = map(int, input().split())
# commands = [tuple(map(int, input().split())) for _ in range(k)]

# # Please write your code here.

N, K = map(int, input().split())

line = [0] * (N + 1)

for _ in range(K):
    start, end = map(int, input().split())
    
    for i in range(start, end + 1):
        line[i] += 1

print(max(line))