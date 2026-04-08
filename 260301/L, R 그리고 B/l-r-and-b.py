SIZE = 10

grid = []
L = ()
R = ()
B = ()

for row in range(SIZE):
    line = list(input())
    grid.append(line)

    for idx in range(SIZE):
        if line[idx] == 'L':
            L = (row, idx)
        elif line[idx] == 'R':
            R = (row, idx)
        elif line[idx] == 'B':
            B = (row, idx)

distance = 0
if (L[0] == R[0] and R[0] == B[0]) or (L[1] == R[1] and R[1] == B[1]):
    # L, R, B가 한 직선상에 있으며, R이 중간에 끼어있을 경우에만 + 2번 추가 이동
    if L[0] < R[0] < B[0] or B[0] < R[0] < L[0] or L[1] < R[1] < B[1] or B[1] < R[1] < L[1]:
        distance = max(abs(B[0] - L[0]), abs(B[1] - L[1])) + 1 # +2 / -1

    else:
        distance = abs(B[0] - L[0]) +  abs(B[1] - L[1]) - 1
else:
    distance = abs(B[0] - L[0]) +  abs(B[1] - L[1]) - 1

print(distance)