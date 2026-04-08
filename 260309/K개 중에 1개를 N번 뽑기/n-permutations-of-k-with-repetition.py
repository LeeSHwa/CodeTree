K, N = map(int, input().split())

list = []

def recurr(depth):
    if depth == N:
        print(*list)
        return
    
    list.append(1)
    recurr(depth + 1)
    list.pop()

    if K >= 2:
        list.append(2)
        recurr(depth + 1)
        list.pop()

        if K >= 3:
            list.append(3)
            recurr(depth + 1)
            list.pop()

            if K == 4:
                list.append(4)
                recurr(depth + 1)
                list.pop()
    
    return

recurr(0)