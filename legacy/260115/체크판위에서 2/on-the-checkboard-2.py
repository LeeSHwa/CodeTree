R, C = map(int, input().split())

grid = [list(input().split()) for _ in range(R)]

'''
1. 색이 달라야 함
2. 적어도 우하단으로 1칸 이상씩 이동해야함
3. 시작, 도착 지점을 제외하고 점프하며 도달한 위치가 정확히 2곳 뿐이어야 합니다.

시작과 끝을 포함하여 총 4번만에 이동해야함
'''

color = grid[0][0]
count = 0

if color == grid[R-1][C-1]:
    print(0)
    exit()

for i in range(1, R - 2): # 1 ~ R-2
    for j in range(1, C - 2):

        if grid[i][j] != color:

            for p in range(i + 1, R - 1): # i + 1 ~ R - 1
                for q in range(j + 1, C - 1):

                    if grid[p][q] == color:
                        count += 1
        #                 print(f"visited ({p}, {q})")
        # print(f"({i}, {j})")
print(count)
        