k, n = map(int, input().split())

array = [0 for _ in range(n)]

def recurr(idx):
    if idx == n:
        print(*array)
        return
    
    for num in range(1, k + 1):
        if idx > 1 and num == array[idx - 1] and array[idx - 1] == array[idx - 2]:
            continue

        array[idx] = num
        recurr(idx + 1)

recurr(0)