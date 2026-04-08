n = int(input())

def print_starts(N):
    if N == 0:
        return
    
    for _ in range(N):
        print("*", end = " ")
    print()
    
    print_starts(N-1)

    for _ in range(N):
        print("*", end = " ")
    print()

print_starts(n)