N = int(input())

def calculator(N):
    if N < 10:
        return N ** 2
    
    return calculator(N // 10) + (N % 10) ** 2
    # 1527, cal(152) return 7

print(calculator(N))