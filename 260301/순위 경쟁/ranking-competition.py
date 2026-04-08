n = int(input())

state = 7 # / 1: A / 2: B / 3: C / 4: A, B / 5: B, C / 6: A, C / 7: A, B, C
cnt = 0
A, B, C = 0, 0, 0

for _ in range(n):
    c, s = input().split()
    s = int(s)
    
    if c == 'A':
        A += s
    elif c == 'B':
        B += s
    else:
        C += s
    

    if A == B and B == C:
        if state != 7:
            state = 7
            cnt += 1
    
    elif A > B and A > C:
        if state != 1:
            state = 1
            cnt += 1
    
    elif B > A and B > C:
        if state != 2:
            state = 2
            cnt += 1

    elif C > B and C > A:
        if state != 3:
            state = 3
            cnt += 1

    elif A == B and A > C:
        if state != 4:
            state = 4
            cnt += 1

    elif B == C and B > A:
        if state != 5:
            state = 5
            cnt += 1

    elif A == C and A > B:
        if state != 6:
            state = 6
            cnt += 1

print(cnt)
        
    