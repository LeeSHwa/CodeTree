n = int(input())

visited = [False] * (n + 1)

ans = []

def backtrack(select_cnt):
    
    if select_cnt == n:
        print(*ans)
        return
    
    for i in range(n, 0, -1):

        if visited[i]:
            continue
        
        visited[i] = True
        ans.append(i)

        backtrack(select_cnt + 1)

        ans.pop()
        visited[i] = False

backtrack(0)