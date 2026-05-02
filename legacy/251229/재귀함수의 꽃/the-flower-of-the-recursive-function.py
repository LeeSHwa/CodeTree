N = int(input())

def flower_of_recurrsion(N):
    if N == 0:
        return
    
    print(N, end=" ")
    flower_of_recurrsion(N-1)
    print(N, end=" ")
    
flower_of_recurrsion(N)