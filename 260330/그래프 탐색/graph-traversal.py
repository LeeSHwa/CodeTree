from collections import defaultdict

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

array = defaultdict(list)

for start, end in edges:
    array[start].append(end)
    array[end].append(start)
    

visited = [False] * (n + 1)
visited[1] = True
ans = 0

def dfs(num):
    global ans

    for next_num in array[num]:
        if not visited[next_num]:
            # print(num, next_num)
            visited[next_num] = True
            dfs(next_num)


dfs(1)

print(visited.count(True) - 1)