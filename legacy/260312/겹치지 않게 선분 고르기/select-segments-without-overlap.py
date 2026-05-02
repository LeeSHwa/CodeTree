n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
array = [0] * 1001
ans = 0

def is_duplicated(a1, a2):
    for idx in range(a1, a2 + 1):
        if array[idx] > 0:
            return True
    
    return False

def apply_var(x1, x2, var):
    for idx in range(x1, x2 + 1):
        array[idx] += var

def recurr(dep, cnt):
    global ans
    if dep == n:
        ans = max(ans, cnt)
        return
        
    curr_x1, curr_x2 = lines[dep]

    if not is_duplicated(curr_x1, curr_x2):
        apply_var(curr_x1, curr_x2, 1)
        recurr(dep + 1, cnt + 1)
        apply_var(curr_x1, curr_x2, -1)
    
    recurr(dep + 1, cnt)

recurr(0, 0)

print(ans)