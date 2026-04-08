N = int(input())

line = [tuple(map(int, input().split())) for _ in range(N)]

lines = [0] * 101

for start, end in line:
    for idx in range(start, end + 1):
        lines[idx] += 1

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            flag = True
            
            curr = lines.copy()
            
            start, end = line[i]
            for idx in range(start, end + 1):
                curr[idx] -= 1

            start, end = line[j]
            for idx in range(start, end + 1):
                curr[idx] -= 1

            start, end = line[k]
            for idx in range(start, end + 1):
                curr[idx] -= 1

            for num in curr:
                if num >= 2:
                    flag = False
                    break

            if flag:
                cnt += 1

print(cnt)