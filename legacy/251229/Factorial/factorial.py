N = int(input())

def Factorial(N):
    if N == 0:
        return 1

    return Factorial(N-1) * N

print(Factorial(N))