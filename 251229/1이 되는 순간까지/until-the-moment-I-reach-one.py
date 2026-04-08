N = int(input())
count = 0

def go_to_one(N):
    global count

    if N == 1:
        return count + 1 
    
    if N % 2 == 0:
        go_to_one(N // 2)
    else:
        go_to_one(N // 3)
    
    count += 1

go_to_one(N)
print(count)