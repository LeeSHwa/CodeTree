n = int(input())

# Please write your code here.
UNUSED = -1
stairs = [UNUSED for _ in range(n + 1)]

def dp(n):
    if stairs[n] != UNUSED:
        return stairs[n]
    
    if n < 5:
        return 1
    
    stairs[n] = dp(n-2) + dp(n-3)

    return stairs[n]

print(dp(n) % 10007)
    