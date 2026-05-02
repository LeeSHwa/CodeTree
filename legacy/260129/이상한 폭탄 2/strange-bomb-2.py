N, K = map(int, input().split())

booms = [int(input()) for _ in range(N)]
is_boom = [False] * (1001)

idx = -1
for i in range(N - 1):

    bound = i + K if i + K < N else N - 1

    if bound < N:
        for j in range(i + 1, bound + 1):
            # print(booms[i], booms[j])
            if booms[i] == booms[j]:
                idx = max(idx, booms[j])

print(idx)