N = int(input())

def cal(N):
    if N == 0:
        return 2
    elif N == 1:
        return 4

    return (cal(N-1) * cal(N-2)) % 100


print(cal(N - 1))
    