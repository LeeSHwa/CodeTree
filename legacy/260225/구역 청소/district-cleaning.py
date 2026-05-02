a, b = map(int, input().split())
c, d = map(int, input().split())

visited = [False] * 101

for idx in range(a, b):
    visited[idx] = True

for idx in range(c, d):
    visited[idx] = True

print(visited.count(True))