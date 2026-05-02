N = int(input())

def print_stars(N):
    if N == 0:
        return
    
    print_stars(N-1)
    print('*' * N)

print_stars(N)