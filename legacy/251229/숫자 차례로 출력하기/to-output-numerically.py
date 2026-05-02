N = int(input())

def recur(N):
    if N == 0:
        return
    
    recur(N-1)
    print(N, end = " ") # 1 -> 2 -> 3
    
def recur_rev(N):
    if N == 0:
        print()
        return
    
    print(N, end = " ") # 3 -> 2 -> 1
    recur_rev(N-1)

recur(N)
print()
recur_rev(N)