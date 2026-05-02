N = int(input())

def recur(N):
    if N == 0:
        return
    print("HelloWorld")
    recur(N-1)

recur(N)