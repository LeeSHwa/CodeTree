N = int(input())

A = 0
B = 0
# A일때는 -1, B일때는 1, 동등일때는 0
honor = 0

cnt = 0

for _ in range(N):
    c, s = input().split()
    s = int(s)
    
    if c == 'A':
        A += s
    else:
        B += s

    if A == B:
        if honor != 0:
            cnt += 1
            honor = 0
    
    elif A > B:
        if honor != -1:
            cnt += 1
            honor = -1
    
    else:
        if honor != 1:
            cnt += 1
            honor = 1

print(cnt)