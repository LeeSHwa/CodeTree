N = int(input())

def cal(N):
    if N <= 0:
        return 0

    return cal(N-2) + N

print(cal(N))