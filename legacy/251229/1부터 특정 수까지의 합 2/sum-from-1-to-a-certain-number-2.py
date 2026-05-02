N = int(input())

def calculate_sum(N):
    if N == 1:
        return 1
    
    return calculate_sum(N-1) + N

print(calculate_sum(N))