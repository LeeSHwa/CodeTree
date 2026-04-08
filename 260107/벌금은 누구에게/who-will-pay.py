N, M, K = map(int, input().split())

students = [0] * N

for _ in range(M):
    ban = int(input())
    students[ban - 1] += 1

    if students[ban - 1] >= K:
        print(ban)
        exit()
    
print(-1)